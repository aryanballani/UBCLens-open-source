<template>
  <div class="home">
    <!-- Navigation Bar -->
    <nav class="navbar">
      <div class="nav-left">
        <h1>UBC Discussions</h1>
      </div>
      <div class="nav-right">
        <button @click="goToHome">Home</button>
        <button @click="goToAbout">About</button>
      </div>
    </nav>

    <!-- Main Content -->
    <div class="content">
      <h2>Welcome to the Course Selection Page</h2>
      <input 
        type="text" 
        v-model="searchQuery" 
        placeholder="Search for a course..." 
        @input="filterCourses"
      />
      
      <ul v-if="filteredCourses.length">
        <li v-for="course in filteredCourses" :key="course.id">{{ course.name }}</li>
      </ul>
      <p v-else>No courses found</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: '',  // Search bar input
      courses: [        // Mock course data
        { id: 1, name: 'Intro to Machine Learning' },
        { id: 2, name: 'Data Structures and Algorithms' },
        { id: 3, name: 'Introduction to Vue.js' },
        { id: 4, name: 'Advanced React' }
      ],
      filteredCourses: []
    };
  },
  methods: {
    filterCourses() {
      // Filters courses based on search query
      this.filteredCourses = this.courses.filter(course =>
        course.name.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    },
    goToHome() {
      // Logic to navigate to home page (can use Vue Router if you have it)
      alert('Navigating to Home!');
    },
    goToAbout() {
      // Logic to navigate to about page (can use Vue Router if you have it)
      alert('Navigating to About!');
    }
  },
  created() {
    // Initially show all courses
    this.filteredCourses = this.courses;
  }
};
</script>

<style scoped>
/* Navigation Bar Styles */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #333;
  padding: 10px;
  color: white;
}

.nav-left h1 {
  margin: 0;
  font-size: 24px;
}

.nav-right button {
  background-color: #4CAF50;
  border: none;
  color: white;
  padding: 10px 20px;
  margin-left: 10px;
  cursor: pointer;
  font-size: 16px;
}

.nav-right button:hover {
  background-color: #45a049;
}

/* Main Content Styles */
.home .content {
  text-align: center;
  margin-top: 20px;
}

input {
  padding: 10px;
  width: 80%;
  margin-bottom: 20px;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  padding: 10px;
  background-color: #f0f0f0;
  margin: 5px 0;
}
</style>
