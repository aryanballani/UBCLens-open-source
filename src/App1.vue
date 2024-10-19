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
        :file="courseFileMap[selectedCourse]"
        @back="selectedCourse = null"
      />
    </v-main>
  </v-app>
</template>

<script setup>
import { ref } from 'vue'
import Course from './components/Course1.vue'

const courses = ref(['CPSC 213'])
const selectedCourse = ref(null)

const courseFileMap = {
  'CPSC 213': './data/CPSC_213_Data_4.csv'
}

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