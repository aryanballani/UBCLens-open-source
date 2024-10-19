<!-- components/LineChart.vue -->
<template>
    <div style="width: 100%; height: 100%;">
      <apexchart
        type="line"
        :options="chartOptions"
        :series="series"
        height="100%"
      />
    </div>
  </template>
  
  <script setup>
  import { ref, watch } from 'vue'
  import VueApexCharts from 'vue3-apexcharts'
  
const props = defineProps(['xAxisData', 'yAxisData'])

const series = ref([{
  name: 'Number of Posts',
  data: []
}])
  
  const chartOptions = ref({
    chart: {
      type: 'line',
      background: 'transparent',
      toolbar: {
        show: false
      }
    },
    colors: ['#42b883'],
    xaxis: {
      categories: [],
      labels: {
        style: {
          colors: '#fff'
        }
      }
    },
    yaxis: {
      title: {
        text: 'Number of Posts',
        style: {
          color: '#fff'
        }
      },
      labels: {
        style: {
          colors: '#fff'
        }
      }
    },
    grid: {
      borderColor: '#555',
      strokeDashArray: 3
    },
    theme: {
      mode: 'dark'
    },
    stroke: {
      width: 2,
      curve: 'smooth'
    },
    markers: {
      size: 4
    }
  })

// Watch for changes in xAxisData and yAxisData props
watch(
  () => [props.xAxisData, props.yAxisData],
  ([newXAxisData, newYAxisData]) => {
    // Update the x-axis categories and series data
    chartOptions.value.xaxis.categories = newXAxisData || [] // Set categories to x-axis data
    series.value[0].data = newYAxisData || [] // Set series data to y-axis data
  },
  { immediate: true }
)

  </script>