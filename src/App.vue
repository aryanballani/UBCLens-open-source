<!-- App.vue -->
<template>
  <v-app theme="dark">
    <!-- Navigation Bar -->
    <v-app-bar color="surface">
      <v-app-bar-title class="text-green">UBC Discussions</v-app-bar-title>
      <v-spacer></v-spacer>
      <v-btn variant="text">View Grades</v-btn>
      <v-btn variant="text">Statistics</v-btn>
      <v-btn variant="text">Help</v-btn>
    </v-app-bar>

    <!-- Main Content -->
    <v-main>
      <v-container class="py-8" v-if="!selectedCourse">
        <v-card class="pa-6">
          <v-card-title class="text-h5 mb-6">View Grades by Section</v-card-title>
          
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

          <!-- Course Grid -->
          <v-row>
            <v-col cols="12" sm="6" md="4" v-for="course in courses" :key="course">
              <v-card
                @click="selectCourse(course)"
                :ripple="true"
                class="course-card"
                variant="outlined"
                hover
              >
                <v-card-title class="text-green">{{ course }}</v-card-title>
              </v-card>
            </v-col>
          </v-row>
        </v-card>
      </v-container>
      
      <!-- Course Component -->
      <Course 
        v-else 
        :courseId="selectedCourse"
        @back="selectedCourse = null"
      />
    </v-main>
  </v-app>
</template>

<script setup>
import { ref } from 'vue'
import Course from './components/Course.vue'

const courses = ref(['CPSC 310', 'SCIE 113', 'CPSC 213'])
const selectedCourse = ref(null)

const selectCourse = (course) => {
  selectedCourse.value = course
}
</script>

<style scoped>
.text-green {
  color: #42b883 !important;
}

.course-card {
  transition: transform 0.2s;
}

.course-card:hover {
  transform: translateY(-2px);
}

:deep(.v-btn) {
  text-transform: none;
}

:deep(.v-card) {
  border-color: #42b883;
}

:deep(.v-select .v-field.v-field--focused) {
  border-color: #42b883;
}
</style>
<script>
import Home from './components/Home.vue'; // Import Home component

export default {
  components: {
    Home,
  },
};
</script>
