<!-- src/App.vue -->
<template>
  <v-app>
    <router-view />
  </v-app>
</template>

<script setup>
import { ref } from 'vue'
import Course from './components/Course.vue'

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
import router from './router';

export default {
  components: {
    Home,
  },
};
</script>