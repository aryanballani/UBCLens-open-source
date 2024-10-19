<!-- src/components/Home.vue -->
<script setup>
import { ref } from 'vue';
import CourseCard from './CourseCard.vue'; // Import CourseCard component

const courses = ref(['CPSC 310', 'SCIE 113', 'CPSC 213']);
</script>

<template>
  <v-app theme="dark">
    <!-- Navigation Bar -->
    <v-app-bar color="surface">
      <v-app-bar-title class="text-green">UBC Discussions</v-app-bar-title>
      <v-spacer></v-spacer>
      <v-btn variant="text">View Discussions</v-btn>
      <v-btn variant="text">Statistics</v-btn>
      <v-btn variant="text">Help</v-btn>
    </v-app-bar>

    <!-- Main Content -->
    <v-main>
      <!-- Search Form Section -->
      <v-container class="py-8" style="background-color: #333;">
        <v-card class="pa-6">
          <v-card-title class="text-h5 mb-6">View Discussions by Section</v-card-title>
          
          <!-- Search Form -->
          <v-row class="mb-6">
            <v-col cols="12" sm="6" md="3">
              <v-select
                label="Year/Session"
                :items="['2023W', '2024W']"
                variant="outlined"
                color="green"
              ></v-select>
            </v-col>
            
            <v-col cols="12" sm="6" md="3">
              <v-select
                label="Subject"
                :items="['CPSC', 'SCIE']"
                variant="outlined"
                color="green"
              ></v-select>
            </v-col>
            
            <v-col cols="12" sm="6" md="3">
              <v-select
                label="Course #"
                :items="['310', '213', '113']"
                variant="outlined"
                color="green"
              ></v-select>
            </v-col>
            
            <v-col cols="12" sm="6" md="3">
              <v-select
                label="Section"
                :items="['001', '002']"
                variant="outlined"
                color="green"
              ></v-select>
            </v-col>
          </v-row>
        </v-card>
      </v-container>

      <!-- Course Grid Section -->
      <v-container class="py-8" style="background-color: #1e1e1e;">
        <v-card class="pa-6">
          <v-row>
            <CourseCard
              v-for="course in courses"
              :key="course"
              :course="course"
            />
          </v-row>
        </v-card>
      </v-container>
    </v-main>
  </v-app>
</template>

<style scoped>
.text-green {
  color: #42b883 !important;
}
</style>
