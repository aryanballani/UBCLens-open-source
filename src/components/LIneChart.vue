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
  import { ref } from 'vue'
  import VueApexCharts from 'vue3-apexcharts'
  
  const series = ref([
    {
      name: 'Students',
      data: [5, 15, 25, 45, 40, 20]
    }
  ])
  
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
      categories: ['0-49%', '50-59%', '60-69%', '70-79%', '80-89%', '90-100%'],
      labels: {
        style: {
          colors: '#fff'
        }
      }
    },
    yaxis: {
      title: {
        text: 'Number of Students',
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
  </script>