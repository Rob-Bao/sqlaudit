<template>
  <el-table
    :data="worklist"
    :default-sort = "{prop: 'work_id',order: 'descending'}"
    element-loading-text="Loading"
    border
    fit
    highlight-current-row
    style="width: 100%;">
    <el-table-column :formatter="formatter" label="DateTime" prop="work_id" align="center" sortable/>
    <!--<el-table-column label="工单ID" prop="work_id" align="center" width="100" sortable />-->
    <el-table-column label="工单标题" prop="workname" align="center" />
    <el-table-column label="数据库名" prop="db_name" align="center" />
    <el-table-column label="执行语句" align="center">
      <template slot-scope="scope">
        <el-button size="small" type="text" icon="el-icon-info" @click="handleSqlDetail(scope.row.db_sql)">详细</el-button>
      </template>
    </el-table-column>
    <!--<el-table-column label="执行语句" prop="db_sql" />-->
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
    <el-table-column label="详情" width="150" align="center" >
      <template slot-scope="scope">
        <el-popover
          v-if="scope.row.work_status <= -1"
          placement="right"
          width="300"
          trigger="click">
          <div align="left" v-html="scope.row.rejected_note" >.</div>
          <el-button slot="reference" size="mini" type="text" icon="el-icon-info">驳回原因</el-button>
        </el-popover>
        <el-button v-if="scope.row.work_status === 3" size="small" type="text" icon="el-icon-info" @click="handleExecResDetail(scope.row.work_id)">执行结果</el-button>
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
      </el-table>
    </el-dialog>
    <el-dialog :append-to-body="true" :visible.sync="dialogSqlDetail" title="SQL详情" width="70%" >
      <div align="left" v-html="sqldetail" >.</div>
    </el-dialog>
  </el-table>
</template>

<script>
import { getExecuteRes } from '@/api/workorder'

export default {
  name: 'Table',
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
      sqldetail: '',
      dialogSqlDetail: false,
      dialogExecResVisible: false,
      activeName: '1',
      list: null,
      flag: true
    }
  },
  methods: {
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
    },
    handleSqlDetail(sqldetail) {
      this.dialogSqlDetail = true
      this.sqldetail = sqldetail.replace(/\n/g, '<br/>')
    },
    handleExecResDetail(work_id) {
      this.dialogExecResVisible = true
      this.listQuery.work_id = work_id
      getExecuteRes(this.listQuery).then(res => {
        this.gridData = res
      })
    }
  }
}
</script>
