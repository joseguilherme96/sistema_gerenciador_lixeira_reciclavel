<script setup lang="js">

// Modulos
import { storeToRefs } from 'pinia';
import { RouterView } from 'vue-router'

//Gerenciadores de estado
import { useUserStore } from "./stores/user.js"

//Compoentes
import MenuNavegacao from './components/template/MenuNavegacao.vue'


const { user } = storeToRefs(useUserStore())

</script>

<template>

  <MenuNavegacao v-if="user"></MenuNavegacao>

  <v-container>

    <RouterView />

  </v-container>

</template>

<style scoped></style>
