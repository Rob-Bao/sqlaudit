<template>
  <div class="app-container">
    <div class="filter-container">
      <el-input v-model="listQuery.workname" size="small" placeholder="工单标题" style="width: 200px;" class="filter-item" @keyup.enter.native="fetchData()"/>
      <el-button class="filter-item" size="small" type="primary" icon="el-icon-search" @click="fetchData()">搜&刷</el-button>
      <router-link :to="'/task/create/'">
        <el-button size="small" type="primary" icon="el-icon-edit">填写工单</el-button>
      </router-link>
      <el-button class="filter-item" size="small" style="margin-left: 10px;" type="primary" icon="el-icon-check" @click="fetchData(0)">未审核</el-button>
    </div>
    <br>
    <table-detail :worklist="workers" />
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
import { getWorkList, updateWork, createWork } from '@/api/workorder'
import { getInfo } from '@/api/login'

export default {
  components: { TableDetail },
  data() {
    return {
      username: '',
      // 分页项
      currentPage1: 1, // 默认页
      pagesizes: [10, 20, 30, 40], // 每页显示条数
      totalrows: 0, // 数据的总条目数
      listQuery: { 'page': 1, 'page_size': 10, 'author': '', 'workname': '' }, // 请求是传递的参数
      //
      workers: [],
      flag: true
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData(status) {
      getInfo().then(res => {
        this.listQuery.author = res.name
        this.listQuery.work_status = status
        getWorkList(this.listQuery).then(res => {
          this.workers = res.results
          // 分页项
          this.totalrows = res.count
          //
        })
      })
    },
    // 分页项
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.fetchData()
      // console.log(`当前页: ${val}`)
    },
    handleSizeChange(val) {
      this.listQuery.page_size = val
      this.fetchData()
      // console.log(`每页 ${val} 条`)
    }
  }
}
</script>
