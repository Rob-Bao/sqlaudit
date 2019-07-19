<template>
  <div class="chart-container">
    <!--<chart height="50%" width="50%"/>-->
  </div>
</template>

<script>
import Chart from '@/components/Charts/lineMarker'

export default {
  name: 'LineChart',
  components: { Chart }
}
</script>

<style scoped>
.chart-container{
  position: relative;
  width: 100%;
  height: calc(100vh - 84px);
}
</style>

