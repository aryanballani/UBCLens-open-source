<!-- src/App.vue -->
<template>
  <v-app>
    <router-view />
  </v-app>
</template>

<script>
import Home from './components/Home.vue'; // Import Home component
import router from './router';

export default {
  components: {
    Home,
  },
};
</script>
