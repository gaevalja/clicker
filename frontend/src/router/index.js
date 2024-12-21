import { createRouter, createWebHistory } from 'vue-router';
import LoginPage from '../views/LoginPage.vue';
import RegisterPage from '../views/RegisterPage.vue';
import HomePage from '../views/HomePage.vue';
import ClickPage from '../views/ClickPage.vue';
import ProfilePage from '../views/ProfilePage.vue';

const routes = [
  { path: '/', name: 'Home', component: HomePage },
  { path: '/auth/login', name: 'Login', component: LoginPage },
  { path: '/auth/register', name: 'Register', component: RegisterPage },
  { path: '/click', name: 'Click', component: ClickPage },
  { path: '/profile', name: 'Profile', component: ProfilePage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;