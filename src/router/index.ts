import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LixeiraView from '@/views/LixeiraView.vue';
import InformarStatusLixeira from '@/views/InformarStatusLixeira.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/lixeiras',
      name: 'lixeiras',
      component: LixeiraView
    },
    {
      path:'/informar-status-lixeira/:id',
      name:'informar-status-lixeira',
      component: InformarStatusLixeira
    }
  ],
})

export default router
