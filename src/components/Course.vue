<!-- components/Course.vue -->
<template>
    <v-container fluid class="pa-0">
      <v-row>
        <!-- Back Button -->
        <v-col cols="12" class="pa-4">
          <v-btn
            prepend-icon="mdi-arrow-left"
            variant="text"
            color="green"
            @click="goBack"
          >
            Back to Courses
          </v-btn>
        </v-col>
      </v-row>
  
      <v-row class="fill-height">
        <!-- Graph Section (Left side) -->
        <v-col cols="12" md="8" class="pa-6">
          <v-card class="h-100">
            <v-card-title class="text-green pb-4">Grade Distribution - {{ courseId }}</v-card-title>
            <div class="graph-container pa-4" style="height: 400px">
              <v-card-text>
                <div style="width: 100%; height: 400px;">
                  <line-chart />
                </div>
              </v-card-text>
            </div>
          </v-card>
        </v-col>
  
        <!-- Right Side Panels -->
        <v-col cols="12" md="4" class="pa-6">
          <!-- Top Panel -->
          <v-card class="mb-6">
            <v-card-title class="text-green">Course Statistics</v-card-title>
            <v-card-text>
              <div class="text-body-1 mb-2">Average Grade: 75.4%</div>
              <div class="text-body-1 mb-2">Pass Rate: 92%</div>
              <div class="text-body-1 mb-2">Total Students: 156</div>
              <div class="text-body-1">Section: 001</div>
            </v-card-text>
          </v-card>
  
          <!-- Bottom Panel -->
          <v-card>
            <v-card-title class="text-green">Course Information</v-card-title>
            <v-card-text>
              <div class="text-body-1 mb-2">
                <strong>Professor:</strong> Dr. Smith
              </div>
              <div class="text-body-1 mb-2">
                <strong>Term:</strong> 2024W
              </div>
              <div class="text-body-1">
                <strong>Description:</strong> Introduction to Software Engineering. 
                Learn about software development lifecycle, testing, and project management.
              </div>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script setup>
  import { defineProps } from 'vue'
  import { useRouter } from 'vue-router'
  import LineChart from './LineChart.vue'
  
  const props = defineProps({
    courseId: {
      type: String,
      required: true
    }
  })
  
  const router = useRouter()
  
  const goBack = () => {
    router.push('/home')
  }
  </script>
  
  <style scoped>
  .text-green {
    color: #42b883 !important;
  }
  
  .graph-container {
    width: 100%;
    height: 100%;
    min-height: 400px;
  }
  
  :deep(.v-card) {
    border-color: #42b883;
  }
  </style>