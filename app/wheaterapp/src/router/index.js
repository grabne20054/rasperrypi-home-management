import { createRouter, createWebHistory } from 'vue-router';
import Login from '../components/LogIn.vue';
import Dashboard from '../components/DashBoard.vue';

const routes = [
  {
    path: '/login',
    component: Login
  },
  {
    path: '/dashboard',
    component: Dashboard,
    beforeEnter: (to, from, next) => {
      if (localStorage.getItem('authenticated') === 'true') {
        next();
      } else {
        next('/login');
      }
    }
  },
  {
    path: '/',
    redirect: '/login'
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
