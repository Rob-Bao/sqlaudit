<template>
  <div class="app-container">
    <div class="filter-container">
      <el-form ref="dataform" :model="listQuery" :inline="true" label-width="100px" >
        <el-form-item label="实例名称">
          <el-select v-model="listQuery.instance_name" size="small" filterable placeholder="可输入选择" clearable>
            <el-option
              v-for="item in instance_list"
              :key="item.instance_name"
              :label="item.instance_name"
              :value="item.instance_name"
              @click.native="fetchDatabase(item.id)">
              <span :instance_port="item.instance_port" style="float: left" >{{ item.instance_name }}</span>
              <span style="float: right; color: #8492a6; font-size: 13px" >{{ item.instance_port }}</span>
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="数据库名">
          <el-select v-model="listQuery.db_name" size="small" filterable placeholder="可输入选择" clearable>
            <el-option
              v-for="item in database_list"
              :key="item.db_name"
              :label="item.db_name"
              :value="item.db_name"
              @click.native="fetchDatatable()"/>
          </el-select>
        </el-form-item>
        <el-form-item label="搜索表名">
          <el-input v-model="listQuery.table_name" size="small" placeholder="输入后回车进行搜索" style="width: 195px;" class="filter-item" clearable @keyup.enter.native="fetchDatatable" @click="fetchDatatable()" />
          <!-- <el-button class="filter-item" size="medium" type="text" icon="el-icon-search" @click="fetchDatatable()">搜索</el-button> -->
        </el-form-item>
      </el-form>
    </div>
    <table-detail :tabledata="tabledata" />
    <div class="block">
      <el-pagination
        :current-page="currentPage1"
        :total="totalrows"
        :page-sizes="pagesizes"
        :page-size="listQuery.page_size"
        layout="total, sizes, prev, pager, next,  jumper"
        @current-change="handleCurrentChange"
        @size-change="handleSizeChange"/>
    </div>
  </div>
</template>

<script>
import TableDetail from './Dropdown/table'
import { getDList } from '@/api/databasetable'
import { getInfo } from '@/api/login'
import { getList, getDBList, CheckMysql } from '@/api/instance'

export default {
  components: { TableDetail },
  data() {
    return {
      // 分页项
      currentPage1: 1, // 默认页
      pagesizes: [10, 50, 100], // 每页显示条数
      totalrows: 0, // 数据的总条目数
      listQuery: { 'page': 1, 'page_size': 10, 'instance_name': '', 'db_name': '', 'table_name': '' }, // 请求是传递的参数
      //
      tabledata: [],
      instance_list: [],
      database_list: [],
      instance_id: { 'instance_id': 0, 'page_size': 100 }
    }
  },
  watch: {
    'listQuery.instance_name': function(newValue, oldValue) {
      this.listQuery.db_name = null
    }
  },
  created() {
    this.fetchInstance()
  },
  methods: {
    fetchInstance() {
      getList(this.instance_online).then(response => {
        this.instance_list = response.results
      })
    },
    fetchDatabase(row) {
      this.instance_id.instance_id = row
      getDBList(this.instance_id).then(response => {
        this.database_list = response.results
      })
    },
    fetchDatatable() {
      getDList(this.listQuery).then(resu => {
        this.tabledata = resu.results
        // 分页项
        this.totalrows = resu.count
        //
      })
    },
    // 分页项
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.fetchDatatable()
      // console.log(`当前页: ${val}`)
    },
    handleSizeChange(val) {
      this.listQuery.page_size = val
      this.fetchDatatable()
      // console.log(`每页 ${val} 条`)
    }
  }
}
</script>
