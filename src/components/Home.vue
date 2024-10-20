<script setup>
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import CourseCard from './CourseCard.vue'; // Import CourseCard component

// Data structure for courses
const courses = ref([
  {
    faculty: "CPSC",
    section: "320",
    image: "../../data/icons/course_img.png",
  },
  {
    faculty: "STAT",
    section: "200",
    image: "../../data/icons/course_img.png",
  },
  {
    faculty: "CPSC",
    section: "213",
    image: "../../data/icons/course_img.png",
  },
  {
    faculty: "hack-",
    section: "la",
    image: "../../data/icons/course_img.png",
  },
  {
    faculty: "WRDS",
    section: "150B",
    image: "../../data/icons/course_img.png",
  },
  {
    faculty: "CPSC",
    section: "210",
    image: "../../data/icons/course_img.png",
  },
  {
    faculty: "PHYS",
    section: "317",
    image: "../../data/icons/course_img.png",
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

const router = useRouter();

// Function to navigate to a course page
const goToCourse = (faculty, section) => {
  router.push(`/course/${faculty}${section}`);
};

</script>

<template>
  <v-app theme="dark">
    <!-- Navigation Bar -->
    <v-app-bar color="surface">
      <v-app-bar-title class="text-green">UBC Lens</v-app-bar-title>
      <v-spacer></v-spacer>
      <v-btn variant="text">Popular courses</v-btn>
      <v-btn variant="text">About</v-btn>
    </v-app-bar>

    <!-- Main Content -->
    <v-main>
      <!-- Search Form Section -->
      <v-container class="py-8" style="background-color: #444;">
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


            <v-col cols="12" sm="6" md="4">
              <v-text-field
                label="Academic Year (For scaling later)"
                variant="outlined"
                color="green"
              ></v-text-field>
            </v-col>

          </v-row>
        </v-card>
      </v-container>

      <!-- Course Grid Section -->
      <v-container class="py-8" style="background-color: #333;">
        <v-card class="pa-6"> 
          <v-row>
            <CourseCard
              v-for="course in filteredCourses"
              :key="course.faculty + course.section"
              :faculty="course.faculty"
              :section="course.section"
              :courseImage="course.image"
              @click="goToCourse(course.faculty, course.section)"
            />
          </v-row>
        </v-card>
      </v-container>

      <v-container class="py-8" style="background-color: #444;">
        <v-row justify="center">
          <v-card class="pa-6">
            <v-card-title class="text-h5 text-center mb-4 font-weight-bold">About</v-card-title>

            <v-card-text class="text-center text-body-1">
              Our application leverages advanced sentiment analysis and count vectorization techniques to identify top keywords, highlighting what's popular in each course. 
              We also provide a graph for each course, showcasing the frequency of discussions over time, helping users gain valuable insights into course engagement.
            </v-card-text>

            <!-- Input Fields for Filtering Courses by Name and Section (Placeholder) -->
            <v-row class="mb-6">
              <!-- Add any additional inputs or filters here if needed -->
            </v-row>
          </v-card>
        </v-row>
      </v-container>


    </v-main>
  </v-app>
</template>
<style scoped>
.text-green {
  color: #42b883 !important;
}
</style>
