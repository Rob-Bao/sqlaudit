<template>
  <el-steps :active="active" align-center>
    <el-step title="步骤 1" description="这是一段很长很长很长的描述性文字" icon="el-icon-edit"/>
    <el-step title="步骤 2" description="这是一段很长很长很长的描述性文字" icon="el-icon-upload"/>
    <el-step title="步骤 3" description="这是一段很长很长很长的描述性文字" icon="el-icon-picture"/>
  </el-steps>
</template>

<script>
export default {
  // 接受父组件的值
  props: {
    active: {
      type: Number,
      require: true,
      default: function() {
        return []
      }
    }
  }
}
</script>

<style scoped>

</style>
