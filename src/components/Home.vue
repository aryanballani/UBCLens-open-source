<script setup>
import { ref, computed } from 'vue';
import CourseCard from './CourseCard.vue'; // Import CourseCard component

// Data structure for courses
const courses = ref([
  {
    faculty: "CPSC",
    section: "310",
    image: "https://via.placeholder.com/300?text=CPSC+310",
  },
  {
    faculty: "SCIE",
    section: "113",
    image: "https://via.placeholder.com/300?text=SCIE+113",
  },
  {
    faculty: "CPSC",
    section: "213",
    image: "https://via.placeholder.com/300?text=CPSC+213",
  },
  {
    faculty: "WRDS",
    section: "150B",
    image: "https://via.placeholder.com/300?text=WRDS+150B",
  },
  {
    faculty: "CPSC",
    section: "210",
    image: "https://via.placeholder.com/300?text=CPSC+210",
  },
  {
    faculty: "PHYS",
    section: "317",
    image: "https://via.placeholder.com/300?text=PHYS+317",
  },
]);

// User input for filtering
const courseQuery = ref('');
const sectionQuery = ref('');

// Input validation for courseQuery to allow only letters and restrict length to 4
const handleCourseInput = (event) => {
  const regex = /^[A-Za-z]+$/;
  if (!regex.test(event.key) || courseQuery.value.length >= 4) {
    event.preventDefault();  // Prevent non-letter and additional characters after 4 letters
  }
};

// Input validation to only allow digits in section input
const handleSectionInput = (event) => {
  const regex = /^[0-9]*$/;
  if (!regex.test(event.key)) {
    event.preventDefault();
  }
};

// Computed property to filter courses based on user input
const filteredCourses = computed(() => {
  return courses.value.filter(course => {
    // Filter by course name if courseQuery is not empty
    const matchesCourseName = courseQuery.value
      ? course.faculty.toLowerCase().includes(courseQuery.value.toLowerCase())
      : true;

    // Filter by section if sectionQuery is not empty
    const matchesSection = sectionQuery.value
      ? course.section.includes(sectionQuery.value)
      : true;

    return matchesCourseName && matchesSection;
  });
});
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

          <!-- Input Fields for Filtering Courses by Name and Section -->
          <v-row class="mb-6">
            <!-- Course Name Filter (Exactly 4 Letters Only) -->
            <v-col cols="12" sm="6" md="4">
              <v-text-field
                v-model="courseQuery"
                label="Search by Course (4 Letters Only)"
                variant="outlined"
                color="green"
                @keypress="handleCourseInput"
                maxlength="4"
              ></v-text-field>
            </v-col>

            <!-- Section Filter (Numbers Only) -->
            <v-col cols="12" sm="6" md="4">
              <v-text-field
                v-model="sectionQuery"
                label="Search by Section (Numbers)"
                variant="outlined"
                color="green"
                type="text"
                @keypress="handleSectionInput"
              ></v-text-field>
            </v-col>
          </v-row>
        </v-card>
      </v-container>

      <!-- Course Grid Section -->
      <v-container class="py-8" style="background-color: #1e1e1e;">
        <v-card class="pa-6">
          <v-row>
            <CourseCard
              v-for="course in filteredCourses"
              :key="course.faculty + course.section"
              :faculty="course.faculty"
              :section="course.section"
              :courseImage="course.image"
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
