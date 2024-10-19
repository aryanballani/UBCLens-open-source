
<template>
    <v-col cols="12" sm="6" md="4">
      <v-card :ripple="true" class="course-card" variant="outlined" hover>
        <!-- Display Course Name as Faculty + Section -->
        <v-card-title class="text-green">{{ faculty }} {{ section }}</v-card-title>
  
        <!-- Display Course Image -->
        <v-img :src="courseImage" alt="Course Image" class="course-image"></v-img>
      </v-card>
    </v-col>
  </template>
  
  <script>
  
  export default {
    props: {
      faculty: {
        type: String,
        required: true,
      },
      section: {
        type: String,
        required: true,
      },
      courseImage: {
        type: String,
        required: true,
      },
      courseId: {
        type: String,
        required: true,
      }
    },
  };
  </script>
  
  
  <style scoped>
  .text-green {
    color: #42b883 !important;
    font-size: 20px;
    font-weight: bold;
  }
  
  .course-image {
    width: 100%;
    height: 150px;
    object-fit: cover;
    margin-top: 10px;
  }
  
  .course-card {
    transition: transform 0.2s;
  }
  
  .course-card:hover {
    transform: translateY(-2px);
  }
  </style>
  