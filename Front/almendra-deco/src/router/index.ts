import { createRouter, createWebHistory } from 'vue-router';
import LoginVue from '@/views/Login/LoginVue.vue';


const routes = [
    { path: '/login', component: LoginVue },
 
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
