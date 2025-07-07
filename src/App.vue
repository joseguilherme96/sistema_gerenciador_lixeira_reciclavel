<template>

  <MenuNavegacao v-if="user"></MenuNavegacao>

  <div class="layout">

    <MenuLateral v-if="exibirMenuLateral"></MenuLateral>

    <v-progress-circular v-if="validandoToken" color="rgb(165, 137, 94)" indeterminate id="progress-circular"
      size="100"></v-progress-circular>

    <v-container v-else class="conteudo">

      <RouterView />

    </v-container>

  </div>

</template>
<script setup lang="js">

// Variavel de ambiente
const { VITE_API_VALIDAR_TOKEN } = import.meta.env

// Modulos
import { storeToRefs } from 'pinia';
import { RouterView } from 'vue-router'
import { ref } from 'vue'

//Navegação programatica
import { useRouter } from 'vue-router';

//Gerenciadores de estado
import { useUserStore } from "./stores/user.js"

//Compoentes
import MenuNavegacao from './components/template/MenuNavegacao.vue'

//Globals
import { userKey } from '@/global.js'
import axios from 'axios';
import MenuLateral from './components/template/MenuLateral.vue';


const { user, exibirMenuLateral, exibiMenuSuperior } = storeToRefs(useUserStore())
const useUser = useUserStore()
const router = useRouter()
const validandoToken = ref(true)

async function validarToken() {

  setTimeout(async () => {

    validandoToken.value = true

    const json = localStorage.getItem(userKey);
    const dadosUsuario = JSON.parse(json)

    useUser.setUser(null)

    if (!dadosUsuario) {

      validandoToken.value = false
      router.push({ path: '/' })

    }

    const res = await axios.post(VITE_API_VALIDAR_TOKEN, dadosUsuario)


    if (res.data.token) {

      useUser.setUser(dadosUsuario)

    } else {

      localStorage.removeItem(userKey)
      router.push({ path: '/' })

    }

    validandoToken.value = false

  }, 1000)

}

//Verifica se a rota é publica
function isRoutePublic(record) {

  return record.meta.routePublic ? true : false

}

//Adiciona proteção de navegação antes da mudança de página de uma rota para outra verificando se a rota é publica ou privada
router.beforeEach(async (to, from, next) => {

  if (to.matched.some(isRoutePublic)) {

    exibiMenuSuperior.value = true
    console.log(exibiMenuSuperior.value)
    next()
    validandoToken.value = false
    return

  }

  if (useUser.user) {

    next()
    return;

  }

  await validarToken()
  next()

})

</script>

<style scoped>
#progress-circular {

  z-index: 1;
  position: absolute;
  left: 100vh;
  top: 30vh;

}

.layout {

  display: flex;

}
</style>
