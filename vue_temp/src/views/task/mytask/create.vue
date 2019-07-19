<template>
  <div class="app-container" align="center" >
    <el-steps :active="form.active" finish-status="success" process-status="finish" align-center>
      <el-step title="填写工单" description=" " icon="el-icon-edit"/>
      <el-step title="审批" description="请选择审批人，将会以邮件方式通知审批人。" icon="el-icon-view"/>
      <el-step title="提交" description="请认真检查填写的相关信息，确认无误后点击提交，提交后可在工单列表中查看工单状态。" icon="el-icon-upload"/>
    </el-steps>
    <zero-detail v-if="form.active === 0" :values="form" @closeMain="closeMain" />
    <one-detail v-if="form.active === 1" :values="form" @closeMain="closeMain"/>
    <two-detail v-if="form.active === 2" :values="form" @closeMain="closeMain"/>

  </div>
</template>

<script>
import ZeroDetail from './Dropdown/zeroform'
import OneDetail from './Dropdown/oneform'
import TwoDetail from './Dropdown/twoform'
import { getInfo } from '@/api/login'

export default {
  name: 'Create',
  components: { ZeroDetail, OneDetail, TwoDetail },
  data() {
    return {
      form: {
        active: 0
      }
    }
  },
  methods: {
    closeMain(val) {
      this.form = val
    },
    prev() {
      if (this.active-- < 0) this.active = 0
    },
    next() {
      if (this.active++ > 2) this.active = 0
    }
  }
}
</script>
