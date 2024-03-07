
import { createApp } from 'vue';
import App from '../App.vue';
import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/home.vue';
import Panier from '../views/panier.vue';
import Pal from '../views/pal.vue';
import Login from '../views/login.vue';
import Catalogue from '../views/catalogue.vue';
import Signup from '../views/signup.vue';
import NotFound from '../views/Notfound.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/panier/:id',
    name: 'Panier',
    component: Panier,
  },
  {
    path: '/catalogue',
    name: 'Catalogue',
    component: Catalogue,
  },
  {
    path: '/pal/:id',
    name: 'Pal',
    component: Pal,
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/:catchAll(.*)',
    component: NotFound,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});
export default router;
const app = createApp(App);
app.use(router);
app.mount('#app');