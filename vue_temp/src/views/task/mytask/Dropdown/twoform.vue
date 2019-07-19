<template>
  <div class="app-container" align="center">
    <el-card class="box-card" style="width: 80%">
      <div slot="header" class="clearfix" >
        <span style="color: green">请确认提交的内容</span>
        <!--<el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>-->
      </div>
      <div class="text item" align="left">
        <div class="app-container"> 工单ID: {{ res_obj.work_id }}</div>
        <div class="app-container"> 工单名称: {{ res_obj.workname }}</div>
        <div class="app-container"> 数据库名: {{ res_obj.db_name }}</div>
        <div class="app-container">
          执行语句:
          <div v-highlight> <!-- 使用指令 -->
            <pre>
              <code style="" v-html="res_obj.formatDbsql">.</code>
            </pre>
          </div>
        </div>
      </div>
    </el-card>
    <div class="app-container">
      <el-button type="primary" @click="prev" >上一步</el-button>
      <router-link :to="'/task/mytask/'">
        <el-button type="success" @click="sub()">提交</el-button>
      </router-link>
    </div>
  </div>
</template>

<script>
import { getInfo } from '@/api/login'
import { getList } from '@/api/instance'
import { createWork } from '@/api/workorder'

export default {
  name: 'TwoDetail',
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
      sql_content: '',
      res_obj: {},
      form: {
        author: ''
      }
    }
  },
  created() {
    this.userInfo()
  },
  methods: {
    prev() {
      this.values.active--
      this.$emit('closeMain', this.values)
    },
    userInfo() {
      getInfo().then(res => {
        this.form.author = res.name
        this.res_obj = Object.assign(this.values, this.form)
        this.res_obj.work_id = parseInt(Math.round(new Date().getTime() / 1000).toString())
        this.res_obj.formatDbsql = this.res_obj.db_sql.replace(/\n/g, '<br/>').replace(/ /g, '&nbsp&nbsp')
        // this.form.userrole = res.roles[0]
      })
    },
    sub() {
      delete this.res_obj.active
      createWork(this.res_obj).then(res => {
        this.$notify({
          title: '成功',
          message: '创建成功',
          type: 'success',
          duration: 2000
        })
      })
    }
  }
}
</script>

<style scoped>
  .text {
    font-size: 14px;
  }

  .item {
    margin-bottom: 18px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }

  .box-card {
    width: 50%;
  }
</style>

