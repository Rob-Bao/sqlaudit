<template>
  <div class="app-container">
    <el-table
      v-loading="listLoading"
      :data="list"
      style="width: 100%"
      element-loading-text="Loading"
      fit
      highlight-current-row>
      <el-table-column align="center" label="加入时间">
        <template slot-scope="scope">
          <!--<span>{{ scope.row.created | parseTime('{y}-{m}-{d} {h}:{i}') }}</span>-->
          <span>{{ scope.row.date_joined }}</span>
        </template>
      </el-table-column>
      <el-table-column align="center" label="用户名" >
        <template slot-scope="scope">
          {{ scope.row.username }}
        </template>
      </el-table-column>
      <el-table-column align="center" label="邮箱" >
        <template slot-scope="scope">
          {{ scope.row.email }}
        </template>
      </el-table-column>
      <el-table-column class-name="status-col" label="当前角色" align="center" sortable prop="online">
        <template slot-scope="scope">
          <el-tag v-if="scope.row.is_superuser === true">管理员</el-tag>
          <el-tag v-if="scope.row.is_superuser === false">使用人</el-tag>
          <el-tag v-if="scope.row.is_staff === true">审批人</el-tag>
        </template>
      </el-table-column>
      <el-table-column label="授权" align="center" >
        <template slot-scope="scope">
          <el-button size="mini" @click.native.prevent="handleChange(scope.row.username)">编辑</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible">
      <el-form ref="dataForm" :rules="rules" :model="temp" label-position="left" label-width="105px" style="width: 400px; margin-left:50px;">
        <el-select v-model="temp.role" clearable placeholder="请选择" >
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value" />
        </el-select>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">cancel</el-button>
        <el-button type="primary" @click="changeRole()">submit</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { getUList } from '@/api/users'
import { getInfo } from '@/api/login'
import { changeURoles } from '@/api/users'
// import { mapGetters } from 'vuex'

export default {
  data() {
    return {
      list: null,
      listLoading: true,
      dialogFormVisible: false,
      dialogStatus: '',
      textMap: {
        create: '授权'
      },
      value: '',
      options: [{ value: 'admin', label: '管理员' }, { value: 'auditor', label: '审批人' }, { value: 'user', label: '使用人' }],
      temp: {},
      rules: {}
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    handleChange(row) {
      this.dialogStatus = 'create'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
      this.temp.user = row
    },
    changeRole() {
      this.$refs['dataForm'].validate(() => {
        if (this.userrole.indexOf('admin') > -1) {
          this.temp.action = 'changeRole'
          changeURoles(this.temp).then((res) => {
            this.dialogFormVisible = false
            this.$notify({
              title: res.type,
              message: res.message,
              type: res.type,
              duration: 5000
            })
            this.fetchData()
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
      getUList(this.listQuery).then(response => {
        this.list = response
        this.listLoading = false
        this.userInfo()
      })
    }
  }
}
</script>
