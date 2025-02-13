<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import MenuNavegacao from './components/template/MenuNavegacao.vue'


</script>

<template>
  <MenuNavegacao></MenuNavegacao>

  
  <v-container>


    
    



    <RouterView />


  </v-container>

</template>

<style scoped></style>
