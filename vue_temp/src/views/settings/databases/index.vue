<template>
  <div class="app-container">
    <div class="filter-container">
      <el-button type="primary" size="small" icon="el-icon-edit" @click.native.prevent="handleCreate" >添加实例</el-button>
    </div>
    <br>
    <el-table
      v-loading="listLoading"
      :data="list"
      element-loading-text="Loading"
      border
      fit
      highlight-current-row>
      <el-table-column label="ID" align="center" width="65" >
        <template slot-scope="scope" >
          {{ scope.row.id }}
        </template>
      </el-table-column>
      <el-table-column label="实例地址" >
        <template slot-scope="scope">
          {{ scope.row.instance_host }}
        </template>
      </el-table-column>
      <el-table-column label="实例名称" width="200" >
        <template slot-scope="scope">
          {{ scope.row.instance_name }}
        </template>
      </el-table-column>
      <el-table-column label="所有者" width="150" >
        <template slot-scope="scope">
          <span>{{ scope.row.author }}</span>
        </template>
      </el-table-column>
      <el-table-column label="端口" width="150" >
        <template slot-scope="scope">
          {{ scope.row.instance_port }}
        </template>
      </el-table-column>
      <el-table-column class-name="status-col" label="是否在线" width="110" align="center" sortable prop="online">
        <template slot-scope="scope">
          <el-tooltip placement="top">
            <div slot="content">{{ scope.row.connect_content }}</div>
            <el-tag :type="scope.row.online === false ? 'primary' : 'success'" >{{ scope.row.online }}</el-tag>
          </el-tooltip>
        </template>
      </el-table-column>
      <el-table-column label="操作" width="90" align="center" >
        <template slot-scope="scope">
          <el-button type="danger" size="small" icon="el-icon-delete" @click="deleteData(scope.row.id)"/>
        </template>
      </el-table-column>
    </el-table>
    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible">
      <el-form ref="dataForm" :rules="rules" :model="temp" label-position="left" label-width="105px" style="width: 400px; margin-left:50px;">
        <el-form-item label="实例地址" prop="instance_host" >
          <el-input v-model="temp.instance_host" style="width: 400px"/>
        </el-form-item>
        <el-form-item label="实例名称" prop="instance_name" >
          <el-input v-model="temp.instance_name" style="width: 400px"/>
        </el-form-item>
        <el-form-item label="实例端口" prop="instance_port" >
          <el-input v-model="temp.instance_port" style="width: 100px"/>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">cancel</el-button>
        <el-button type="primary" @click="dialogStatus==='create'?createData():updateData()">submit</el-button>
      </div>
    </el-dialog>
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
import { getList, deleteAction, createAction } from '@/api/instance'
import { getInfo } from '@/api/login'
import { checkPerms } from '@/utils/auth'
// import { mapGetters } from 'vuex'

export default {
  data() {
    return {
      username: '',
      userrole: '',
      // 分页项
      currentPage1: 1, // 默认页
      pagesizes: [10, 20, 30, 40], // 每页显示条数
      totalrows: 0, // 数据的总条目数
      listQuery: { 'page': 1, 'page_size': 10 }, // 请求是传递的参数
      //
      list: null,
      listLoading: true,
      temp: {
        instance_host: '',
        instance_name: '',
        instance_port: '',
        author: ''
      },
      dialogFormVisible: false,
      dialogStatus: '',
      textMap: {
        create: 'Create'
      },
      rules: {
        instance_host: [{ required: true, message: '实例地址不可为空', trigger: 'blur' }],
        instance_name: [{ required: true, message: '实例名称不可为空', trigger: 'blur' }],
        instance_port: [{ required: true, message: '端口号不可为空', trigger: 'blur' }, { match: true, 'pattern': '^([3-9]\\d{3}|[1-5]\\d{4}|6[0-4]\\d{3}|65[0-4]\\d{2}|655[0-2]\\d|6553[0-5])$', message: '填写内容必须是3000-65535内的整数！' }]
      }
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    // 分页项
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.fetchData()
      console.log(`当前页: ${val}`)
    },
    handleSizeChange(val) {
      this.listQuery.page_size = val
      this.fetchData()
      console.log(`每页 ${val} 条`)
    },
    // 删除实例项
    deleteData(id) {
      console.log(id)
      this.$confirm('此操作将永久删除该记录, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        deleteAction(id).then(res => {
          this.$notify({
            message: '删除成功',
            type: 'success'
          })
          this.fetchData()
        })
      }).catch(() => {
        this.$notify({
          type: 'info',
          message: '已取消删除'
        })
      })
    },
    resetTemp() {
      this.temp = {
        instance_host: '',
        instance_name: '',
        instance_port: '',
        online: false
      }
    },
    handleCreate() {
      this.resetTemp()
      this.dialogStatus = 'create'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    createData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          this.temp.author = this.username
          createAction(this.temp).then(() => {
            this.list.unshift(this.temp)
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '创建成功',
              type: 'success',
              duration: 2000
            })
          })
        }
      })
    },
    userInfo() {
      getInfo().then(res => {
        this.username = res.name
        this.userrole = res.roles[0]
      })
    },
    fetchData() {
      this.listLoading = true
      getList(this.listQuery).then(response => {
        // 分页项
        this.totalrows = response.count
        //
        this.list = response.results
        this.listLoading = false
        this.userInfo()
      })
    }
  }
}
</script>
