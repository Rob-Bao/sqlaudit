<template>
  <div class="app-main" align="center">
    <el-form ref="sform" :model="form" :rules="rules" :inline="true">
      <!--<h5>想想这页是不是可以加点东西</h5>-->
      <el-form-item label="选择审批人员:" prop="auditer" >
        <el-select v-model="form.auditor" filterable placeholder="可直接搜索审批人" clearable @click.native="fetchUserData()" >
          <el-option
            v-for="item in auditer_list"
            v-if="item.is_staff === true"
            :key="item.username"
            :label="item.username"
            :value="item.username"/>
        </el-select>
      </el-form-item>
    </el-form>
    <div slot="footer" class="dialog-footer">
      <el-button type="primary" @click="prev" >上一步</el-button>
      <el-button v-if="form.auditor==='' ? disabled:'true'" type="success" @click="next">下一步</el-button>
    </div>
  </div>
</template>

<script>
import { getUList } from '@/api/users'

export default {
  name: 'OneDetail',
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
      auditer_list: [],
      res_obj: {},
      disabled: false,
      form: {
        auditor: ''
      },
      rules: {
        auditor: [
          { required: true, message: '请选择审批人', trigger: 'change' }
        ]
      }
    }
  },
  methods: {
    fetchUserData() {
      getUList(this.listQuery).then(response => {
        this.auditer_list = response
      })
    },
    next() {
      this.values.active++
      this.res_obj = Object.assign(this.values, this.form)
      this.$emit('closeMain', this.res_obj)
    },
    prev() {
      this.values.active--
      this.$emit('closeMain', this.values)
    }
  }
}
</script>

<style scoped>
</style>

