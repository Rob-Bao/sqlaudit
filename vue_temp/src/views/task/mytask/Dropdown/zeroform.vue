<template>
  <div class="admin-container" >
    <el-form ref="workform" :model="form" :rules="rules" label-width="100px" @click="fetchInstance">
      <el-form-item label="工单名称" prop="workname" placeholder="请输入工单名称" style="width: 40%">
        <el-input v-model="form.workname" maxlength="50">
          <template slot="prepend">SQL工单-</template>
        </el-input>
      </el-form-item>
      <el-form-item label="选择实例" prop="instance" style="width: 40%">
        <el-select v-model="form.instance" :disabled="check_res === false ? disabled:true" filterable placeholder="请选择" style="width: 100%" clearable>
          <el-option
            v-for="item in instance_list"
            :key="item.instance_host"
            :label="item.instance_name"
            :value="item.instance_host"
            @click.native="fetchDatabase(item.id)">
            <span :instance_port="item.instance_port" style="float: left" >{{ item.instance_name }}</span>
            <span style="float: right; color: #8492a6; font-size: 13px" >{{ item.instance_host }}</span>
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="选择库名" prop="db_name" style="width: 40%" >
        <el-select v-model="form.db_name" :disabled="check_res === false ? disabled:true" filterable placeholder="请选择" style="width: 100%">
          <el-option
            v-for="item in database_list"
            :key="item.db_name"
            :label="item.db_name"
            :value="item.db_name"/>
        </el-select>
      </el-form-item>
      <el-form-item label="SQL内容" prop="db_sql" style="width: 60%">
        <el-input v-model="form.db_sql" :rows="10" :disabled="check_res === false ? disabled:true" type="textarea" placeholder="请输入SQL" >{{ form.name }}</el-input>
      </el-form-item>
    </el-form>
    <div class="app-container" >
      <el-dialog :visible.sync="dialogTableVisible" title="SQL自动审核结果" align="left">
        <div v-if="check_res<1" style="color: blue">#--[Mysql Error 2576 ......]，"语法问题/结尾没有分号/有中文符号" 所导致，请仔细检查语法。 </div>
        <div><hr></div>
        <ul>
          <li v-for="vu in check_content" v-if="vu.errlevel >0" :key="vu.ID" >
            <p style="color: green">ID: {{ vu.ID }}</p>
            <p>Stage: {{ vu.stage }}</p>
            <p>ErrLevel: {{ vu.errlevel }}</p>
            <p>StageStatus: {{ vu.stagestatus }}</p>
            <div>
              <div style="color: blue">ErrorMessage【请按照红字提示信息进行修改】:</div>
              <div style="color: red" v-html="vu.errormessage">.</div>
            </div>
            <br>
            <div>
              <div style="color: blue">SQL语句:</div>
              <div style="color: green" v-html="vu.SQL.replace(/\n/g, '<br/>')">.</div>
            </div>
            <p>AffectedRows: {{ vu.Affected_rows }}</p>
            <p>Sequence: {{ vu.sequence }}</p>
            <p>Backup_Dbname: {{ vu.backup_dbname }}</p>
            <p>Execute_Time: {{ vu.execute_time }}</p>
            <p>SqlSha1: {{ vu.sqlsha1 }}</p>
          </li>
        </ul>
        <div slot="footer" class="dialog-footer">
          <el-button type="info" @click="dialogTableVisible = false" >Close</el-button>
        </div>
      </el-dialog>
      <div class="filter-container">
        <router-link :to="'/task/create/'">
          <el-button v-if="check_res >= 1" type="info" @click="reset">重新填</el-button>
        </router-link>
        <el-button v-if="form.db_sql==='' ||form.workname===''||form.db_name===''||form.instance===''|| check_res>=1 ? disabled:'true'" type="primary" @click="checkSql" >Check</el-button>
        <el-button v-if="form.workname==='' || check_res===false ? disabled:'true'" type="success" @click="next">下一步</el-button>
      </div>
    </div>

  </div>
</template>

<script>
import { getList, getDBList, CheckMysql } from '@/api/instance'

export default {
  name: 'ZeroDetail',
  props: {
    values: {
      type: Object,
      require: true,
      default: function() {
        return []
      }
    }
  },
  data() {
    return {
      dialogTableVisible: false,
      res_obj: {},
      check_res: false,
      check_su: false,
      check_content: '',
      form: {
        workname: '',
        db_name: '',
        instance: '',
        db_sql: '',
        active: 0
      },
      instance_port: 0,
      instance_id: { 'instance_id': 0, 'page_size': 100 },
      instance_online: { 'online': true },
      instance_list: [],
      database_list: [],
      check_dic: { 'instance_host': '', 'dbname': '', 'sql': '', 'execute': 0 },
      disabled: false,
      rules: {
        workname: [
          { required: true, message: '请填写工单名称', trigger: 'blur' },
          { max: 50, message: '长度最大 50 个字符', trigger: 'blur' }
        ],
        db_sql: [
          { required: true, message: '请输入SQL内容', trigger: 'blur' },
          { max: 2000, message: '长度最大 20000 个字符', trigger: 'blur' }
          // { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
        ],
        instance: [
          { required: true, message: '请选择实例名称', trigger: 'change' }
        ],
        db_name: [
          { required: true, message: '请选择数据库名', trigger: 'change' }
        ]
      }
    }
  },
  watch: {
    'form.instance': function(newValue, oldValue) {
      this.form.db_name = null
    }
  },
  created() {
    this.fetchInstance()
  },
  methods: {
    reset() {
      this.$refs.workform.resetFields()
      this.check_res = false
    },
    checkSql() {
      this.check_dic.dbname = this.form.db_name
      this.check_dic.execute = 0
      this.check_dic.instance_host = this.form.instance
      this.check_dic.instance_port = this.database_list[0].instance_port
      this.check_dic.sql = this.form.db_sql
      if (this.check_res === false) {
        CheckMysql(this.check_dic).then(response => {
          this.check_content = response
          for (this.check_res in response) {
            if (response[this.check_res]['errlevel'] > 0) {
              this.check_res = false
              this.dialogTableVisible = true
              break
            }
          }
          if (this.dialogTableVisible === false) {
            this.$message({
              showClose: true,
              message: '恭喜你，SQL审核成功，请点击下一步。',
              type: 'success'
            })
          }
        })
      }
    },
    fetchDatabase(row) {
      this.instance_id.instance_id = row
      getDBList(this.instance_id).then(response => {
        this.database_list = response.results
      })
    },
    fetchInstance() {
      getList(this.instance_online).then(response => {
        this.instance_list = response.results
        this.form.db_name = ''
      })
    },
    next() {
      this.form.active++
      this.form.db_port = this.database_list[0].instance_port
      this.res_obj = Object.assign(this.values, this.form)
      this.$emit('closeMain', this.res_obj)
    }
  }
}
</script>

<style scoped>
</style>

