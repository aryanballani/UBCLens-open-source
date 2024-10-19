<!-- src/components/CourseCard.vue -->
<template>
    <v-col cols="12" sm="6" md="4">
      <v-card :ripple="true" class="course-card" variant="outlined" hover>
        <v-card-title class="text-green">{{ course }}</v-card-title>
      </v-card>
    </v-col>
  </template>
  
  <script>
  export default {
    props: {
      course: {
        type: String,
        required: true,
      },
    },
  };
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
  </style>
  