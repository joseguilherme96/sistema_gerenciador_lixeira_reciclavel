<script setup lang="ts">
import ButtonPadrao from '@/components/ButtonPadrao.vue';

</script>

<template>

  <v-container>
    <v-row>
      <v-col cols="12" sm="6" md="4">
        <v-card color="gray">
          <v-card-title>Grupo de Lixeiras</v-card-title>
          <v-card-text>
            <ButtonPadrao>Acessar</ButtonPadrao>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" sm="6" md="4">
        <v-card>
          <v-card-title>Lixeiras</v-card-title>
          <v-card-text>
            <ButtonPadrao>Acessar</ButtonPadrao>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" sm="6" md="4">
        <v-card>
          <v-card-title>Filtros</v-card-title>
          <v-card-text>
            <ButtonPadrao>Acessar</ButtonPadrao>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>


</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
