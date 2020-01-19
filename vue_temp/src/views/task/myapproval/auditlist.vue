<template>
  <div class="app-container">
    <div class="filter-container">
      <el-button v-if="userrole==='auditor'" class="filter-item" size="small" style="margin-left: 10px;" type="primary" icon="el-icon-check" @click="fetchData(0)">未审核</el-button>
      <el-button v-if="userrole==='admin'" class="filter-item" size="small" style="margin-left: 10px;" type="warning" icon="el-icon-warning" @click="fetchData(1)">未执行</el-button>
      <el-button class="filter-item" size="small" style="margin-left: 10px;" type="success" icon="el-icon-check" @click="fetchData(3)">已完成</el-button>
      <el-button class="filter-item" size="small" style="margin-left: 10px;" type="danger" icon="el-icon-close" @click="fetchData(-1)">已驳回</el-button>
      <!-- <el-form-item label="搜索表名"> -->
      <el-input v-model="listQuery.workname" size="small" placeholder="工单标题" style="width:200px;margin-left:50px;" class="filter-item" clearable @keyup.enter.native="fetchData()" />
      <el-button class="filter-item" size="medium" type="text" icon="el-icon-search" @click="searchData">搜索</el-button>
      <!-- </el-form-item> -->
    </div>
    <br>
    <table-detail :worklist="audit" @upWorkstatus="upWorkstatus" />
    <div class="block">
      <el-pagination
        :current-page="currentPage1"
        :total="totalrows"
        :page-sizes="pagesizes"
        :page-size="listQuery.page_size"
        :page="1"
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
      row: '',
      username: '',
      userrole: '',
      work_status: '',
      // 分页项
      currentPage1: 1, // 默认页
      pagesizes: [5, 10, 20, 30, 40], // 每页显示条数
      totalrows: 0, // 数据的总条目数
      listQuery: { 'page': 1, 'page_size': 10 }, // 请求是传递的参数
      //
      audit: [],
      rejected: [],
      through: [],
      flag: true
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    searchData() {
      this.listQuery.page = 1
      this.fetchData()
    },
    fetchData(status) {
      if (this.work_status !== status) {
        this.listQuery.page = 1
      }
      this.listQuery.work_status = status
      this.work_status = status
      getInfo().then(res => {
        this.username = res.name
        this.userrole = res.roles[0]
        if (this.userrole === 'admin') {
          getWorkList(this.listQuery).then(resu => {
            this.audit = [resu.results]
            this.audit.splice(1, 0, 1)
            this.totalrows = resu.count
            this.next = resu.next
            this.previous = resu.previous
          })
        } else {
          this.listQuery.auditor = this.username
          getWorkList(this.listQuery).then(resu => {
            this.audit = [resu.results]
            this.audit.splice(1, 0, 0)
            // 分页项
            this.totalrows = resu.count
            //
          })
        }
      })
    },
    upWorkstatus(val) {
      if (this.userrole === 'admin') {
        val.datas.dba = this.username
      }
      if (val.datas.work_status === 1 || val.datas.work_status === 2) {
        updateWork(val.id, val.datas).then(res => {
          this.$message({
            title: '成功',
            message: '您已经批准执行该工单',
            type: 'success'
          }, this.fetchData())
        })
      } else {
        this.$prompt('请输入驳回理由', '是否确认驳回？', {
          confirmButtonText: '确定',
          cancelButtonText: '取消'
        }).then(({ value }) => {
          if (this.userrole === 'admin') {
            val.datas.rejected_note = '管理员驳回:' + value
          } else {
            val.datas.rejected_note = '审核员驳回:' + value
          }
          updateWork(val.id, val.datas).then(res => {
            this.$message({
              title: '成功',
              type: 'success',
              message: '您选择驳回该工单'
            }, this.fetchData())
          })
        }).catch(() => {
          this.$message({
            title: '取消',
            type: 'info',
            message: '您选择撤销驳回'
          })
        })
      }
    },
    // 分页项
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.fetchData(this.work_status)
      // console.log(`当前页: ${val}`)
    },
    handleSizeChange(val) {
      this.listQuery.page_size = val
      this.fetchData(this.work_status)
      // console.log(`每页 ${val} 条`)
    }
  }
}
</script>
