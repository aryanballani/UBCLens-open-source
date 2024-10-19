// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/components/Home.vue';
import Course from '@/components/Course.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/course/:courseId',
    name: 'Course',
    component: Course,
    props: true  // Enables passing the route parameter as a prop to the component
  }
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;
