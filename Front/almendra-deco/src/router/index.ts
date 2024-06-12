import { createRouter, createWebHistory } from 'vue-router';
import HomeVue from '@/views/Home/HomeVue.vue';
import LoginVue from '@/views/Login/LoginVue.vue';
import ProductosVue from '@/views/Productos/ProductosVue.vue'


const routes = [
  { path: '/home', name: 'home', component: HomeVue },
  { path: '/login', name: 'Login', component: LoginVue },
  { path: '/productos', name: 'Productos', component: ProductosVue },
  
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
