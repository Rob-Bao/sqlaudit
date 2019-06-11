<template>
  <el-table
    :data="tabledata"
    style="width: 100%">
    <el-table-column type="expand">
      <template slot-scope="props">
        <el-form label-position="left" inline class="demo-table-expand">
          <el-form-item label="数据库名">
            <span>{{ props.row.db_name }}</span>
          </el-form-item>
          <el-form-item label="实例地址">
            <span>{{ props.row.instance_host }}</span>
          </el-form-item>
          <el-form-item label="表名">
            <span>{{ props.row.table_name }}</span>
          </el-form-item>
          <el-form-item label="实例名称">
            <span>{{ props.row.instance_name }}</span>
          </el-form-item>
          <el-form-item label="实例端口">
            <span>{{ props.row.instance_port }}</span>
          </el-form-item>
          <el-form-item label="表大小">
            <span>{{ props.row.table_size }}M</span>
          </el-form-item>
          <el-form-item label="表结构" style="width: 100%">
            <div align="left" style="color: green" v-html="props.row.table_structure.replace(/ /g,'&nbsp&nbsp').replace(/\n/g, '<br/>')" >.</div>
          </el-form-item>
        </el-form>
      </template>
    </el-table-column>
    <el-table-column
      label="表名"
      prop="table_name"/>
    <el-table-column
      label="数据库名"
      prop="db_name"/>
    <el-table-column
      label="实例名称"
      prop="instance_name"/>
  </el-table>
</template>

<style>
  .demo-table-expand {
    font-size: 0;
  }
  .demo-table-expand label {
    width: 90px;
    color: #99a9bf;
  }
  .demo-table-expand .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
    width: 50%;
  }
</style>

<script>
export default {
  name: 'DTable',
  props: {
    tabledata: {
      type: Array,
      require: true,
      default: function() {
        return []
      }
    }
  },
  data() {
    return {
    }
  }
}
</script>
