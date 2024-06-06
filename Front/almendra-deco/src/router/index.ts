import { createRouter, createWebHistory } from 'vue-router';
import HomeVue from '@/views/Home/HomeVue.vue';
import LoginVue from '@/views/Login/LoginVue.vue';


const routes = [
  { path: '/home', name: 'home', component: HomeVue },
  { path: '/login', name: 'Login', component: LoginVue },
  
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
