import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import GrupoLixeiraView from '@/views/GrupoLixeiraView.vue';
import InformarStatusLixeira from '@/views/InformarStatusLixeira.vue';
import LoginView from '@/views/LoginView.vue';
import RelatorioLixeiraView from '@/views/RelatorioLixeiraView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/home',
      name: 'home',
      meta: { routePublic: true, nameFormat: "Home" },
      component: HomeView,
    },
    {
      path: '/about',
      name: 'Painel de Controle',
      meta: { nameFormat: "Sobre" },
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/lixeiras',
      name: 'lixeiras',
      meta: { nameFormat: "Lixeiras" },
      component: GrupoLixeiraView
    },
    {
      path: '/informar-status-lixeira/:id',
      name: 'informar-status-lixeira',
      meta: { routePublic: true, nameFormat: "Informar Status Lixeira" },
      component: InformarStatusLixeira
    },
    {
      path: '/',
      name: 'login',
      component: LoginView
    },
    {
      path: '/relatorio-lixeira',
      name: "relatorio-lixeira",
      meta: { nameFormat: "Relatório Lixeira" },
      component: RelatorioLixeiraView
    }
  ],
})

export default router
