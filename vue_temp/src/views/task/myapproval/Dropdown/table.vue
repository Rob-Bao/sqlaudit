<template>
  <el-table
    :data="worklist[0]"
    :default-sort = "{prop: 'work_id',order: 'descending'}"
    element-loading-text="Loading"
    border
    fit
    highlight-current-row
    style="width: 100%;">
    <el-table-column :formatter="formatter" label="DateTime" prop="work_id" align="center" sortable/>
    <!--<el-table-column label="工单ID" prop="work_id" align="center" width="100" sortable/>-->
    <el-table-column label="工单标题" prop="workname" align="left"/>
    <el-table-column label="实例" prop="instance" align="left" />
    <el-table-column label="数据库名" prop="db_name" align="left" />
    <el-table-column label="执行语句" align="center">
      <template slot-scope="scope">
        <el-button size="small" type="text" icon="el-icon-info" @click="handleSqlDetail(scope.row.db_sql)">详细</el-button>
      </template>
    </el-table-column>
    <el-table-column label="发起者" width="150" align="center" prop="author" />
    <el-table-column label="审批人" width="150" align="center" prop="auditor" />
    <el-table-column label="执行人" width="150" align="center" prop="dba" />
    <el-table-column label="工单状态" width="150" align="center" >
      <template slot-scope="scope">
        <el-tag v-if="scope.row.work_status === 0" type="info">等待审核</el-tag>
        <el-tag v-if="scope.row.work_status === 1" type="warning" >等待执行</el-tag>
        <el-tag v-if="scope.row.work_status === 2" type="success" >后台操作中</el-tag>
        <el-tag v-if="scope.row.work_status === 3" type="success" >工单完成</el-tag>
        <el-tag v-if="scope.row.work_status === -1" type="danger" >已被驳回</el-tag>
      </template>
    </el-table-column>
    <el-table-column label="操作&详情" width="150" align="center" >
      <template slot-scope="scope">
        <el-button v-if="worklist[1]===1 && scope.row.work_status === 1" :click="work_id=scope.row.id" type="success" size="mini" icon="el-icon-check" circle @click="dialogFormVisible=true" />
        <el-button v-if="worklist[1]===1 && scope.row.work_status === 1" type="danger" size="mini" icon="el-icon-close" circle @click="rejected_func(scope.row.id)" />
        <el-button v-if="worklist[1]===0 && scope.row.work_status === 0 " type="success" size="mini" icon="el-icon-check" circle @click="through_func(scope.row.id)"/>
        <el-button v-if="worklist[1]===0 && scope.row.work_status === 0 " type="danger" size="mini" icon="el-icon-close" circle @click="rejected_func(scope.row.id)" />
        <!--<el-button v-if="worklist[1]===1 && scope.row.work_status === 1" type="danger" size="mini" icon="el-icon-close" @click="exec(scope.row.id, -1)"/>-->
        <el-popover
          v-if="scope.row.work_status <= -1"
          placement="right"
          width="300"
          trigger="click">
          <div align="left" v-html="scope.row.rejected_note" >.</div>
          <el-button slot="reference" size="mini" type="text" icon="el-icon-info">驳回原因</el-button>
        </el-popover>
        <el-button v-if="scope.row.work_status === 3" size="small" type="text" icon="el-icon-info" @click="handleExecResDetail(scope.row.id, scope.row.work_id)">执行结果</el-button>
        <el-dialog :visible.sync="dialogFormVisible" title="提交任务" width="30%">
          <el-form :model="form">
            <el-form-item :label-width="formLabelWidth" label="执行方式" align="left">
              <el-radio-group v-model="form.exec_way" >
                <el-radio label="1" >自动执行</el-radio>
                <el-radio label="2" @click.native="handleWay(2)" >手动执行</el-radio>
              </el-radio-group>
            </el-form-item>
            <el-form-item v-if="form.exec_way==='1'" :label-width="formLabelWidth" label="选择时段" align="left">
              <el-radio-group v-model="form.exec_timepoint" >
                <el-radio label="1">立即执行</el-radio>
                <el-radio label="2">明日凌晨02:00后执行</el-radio>
              </el-radio-group>
            </el-form-item>
          </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button @click="dialogFormVisible = false">取 消</el-button>
            <el-button type="primary" @click="through_Action">确 定</el-button>
          </div>
        </el-dialog>
      </template>
    </el-table-column>
    <el-dialog :append-to-body="true" :visible.sync="dialogExecResVisible" title="执行结果" width="70%">
      <el-table :data="gridData">
        <el-table-column property="c_time" label="执行完成时间" width="150"/>
        <el-table-column label="执行状态" width="150">
          <template slot-scope="scope">
            <el-tag v-if="scope.row.exec_status === 1" type="success">执行成功</el-tag>
            <el-tag v-if="scope.row.exec_status === -1" type="danger" >执行失败</el-tag>
          </template>
        </el-table-column>
        <el-table-column property="errormessage" label="错误信息" width="200"/>
        <el-table-column property="SQL" label="SQL内容"/>
        <el-table-column v-if="worklist[1]===1" label="操作">
          <template slot-scope="scope">
            <el-button v-if="scope.row.exec_status === -1" size="small" type="danger" icon="el-icon-warning" @click="dialogFormVisible=true">重置任务</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-dialog>
    <el-dialog :append-to-body="true" :visible.sync="dialogSqlDetail" center="true" style="" title="SQL详情" width="90%" >
      <div v-highlight> <!-- 使用指令 -->
        <pre>
            <code style="" v-html="sqldetail">.</code>
        </pre>
      </div>
    </el-dialog>
  </el-table>
</template>

<script>
import { getInfo } from '@/api/login'
import { getExecuteRes } from '@/api/workorder'

export default {
  name: 'AuditTable',
  props: {
    worklist: {
      type: Array,
      require: true,
      default: function() {
        return []
      }
    }
  },
  data() {
    return {
      gridData: [],
      listQuery: { 'work_id': 0 },
      dialogExecResVisible: false,
      dialogSqlDetail: false,
      sqldetail: false,
      disabled: false,
      dialogFormVisible: false,
      work_id: 0,
      form: {
        exec_timepoint: '1',
        exec_way: '1',
        work_status: 2
      },
      pickerOptions1: {
        disabledDate(time) {
          return time.getTime() > Date.now()
        },
        shortcuts: [{
          text: '今天',
          onClick(picker) {
            picker.$emit('pick', new Date())
          }
        }, {
          text: '明天',
          onClick(picker) {
            const date = new Date()
            date.setTime(date.getTime() + 3600 * 1000 * 24)
            picker.$emit('pick', date)
          }
        }]
      },
      formLabelWidth: '120px',
      userrole: 0,
      // work_status = 0 默认状态，待审核状态。
      param: { 'datas': { 'work_status': 0 }, 'id': 0 },
      activeName: '1',
      list: null,
      flag: true
    }
  },
  created() {
    this.getUserInfo()
  },
  methods: {
    handleSqlDetail(sqldetail) {
      this.dialogSqlDetail = true
      this.sqldetail = sqldetail.replace(/\n/g, '<br/>')
    },
    handleWay(action) {
      if (action === 2) {
        this.form.exec_timepoint = 0
      }
    },
    through_Action() {
      this.param.id = this.work_id
      this.param.datas = this.form
      this.$emit('upWorkstatus', this.param)
      this.dialogFormVisible = false
    },
    getUserInfo() {
      getInfo().then(res => {
        if (res.roles[0] === 'admin') {
          this.userrole = 1
        }
      })
    },
    through_func(id) {
      // work_status=1 表示审批成功，交由管理员操作。
      this.param.datas.work_status = 1
      this.param.id = id
      this.$emit('upWorkstatus', this.param) // closeMain为父组件函数
    },
    rejected_func(id) {
      this.param.datas.work_status = -1
      this.param.id = id
      this.$emit('upWorkstatus', this.param)
    },
    handleExecResDetail(taskid, work_id) {
      this.work_id = taskid
      this.dialogExecResVisible = true
      this.listQuery.work_id = work_id
      getExecuteRes(this.listQuery).then(res => {
        this.gridData = res
      })
    },
    formatter(row) {
      const daterc = row['work_id']
      const dateMat = new Date(daterc * 1000)
      const year = dateMat.getFullYear()
      const month = dateMat.getMonth() + 1
      const day = dateMat.getDate()
      const hh = dateMat.getHours()
      const mm = dateMat.getMinutes()
      const ss = dateMat.getSeconds()
      if (mm < 10) {
        const mms = '0' + mm
        const timeformat = year + '-' + month + '-' + day + ' ' + hh + ':' + mms + ':' + ss
        return timeformat
      } else if (hh < 10) {
        const hhs = '0' + hh
        const timeformat = year + '-' + month + '-' + day + ' ' + hhs + ':' + mm + ':' + ss
        return timeformat
      } else if (ss < 10) {
        const sss = '0' + ss
        const timeformat = year + '-' + month + '-' + day + ' ' + hh + ':' + mm + ':' + sss
        return timeformat
      } else {
        const timeformat = year + '-' + month + '-' + day + ' ' + hh + ':' + mm + ':' + ss
        return timeformat
      }
    }
  }
}
</script>
