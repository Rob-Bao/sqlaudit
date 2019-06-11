<template>
  <div class="dashboard-container">
    <div class="dashboard-text">username:{{ name }}</div>
    <div class="dashboard-text">roles:<span v-for="role in roles" :key="role">{{ role }}</span></div>
    <div class="dashboard-text">perms:{{ perms }}</div>
    <el-button v-if="addPerm">lalallalala</el-button>

  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { checkPerms } from '@/utils/auth'

export default {
  name: 'Dashboard',
  computed: {
    ...mapGetters([
      'name',
      'roles',
      'perms'
    ]),
    addPerm: function() {
      return checkPerms('api.add_dtabaseinfo')
    }
  }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
.dashboard {
  &-container {
    margin: 30px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
</style>
