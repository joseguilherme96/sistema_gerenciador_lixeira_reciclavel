<script setup lang="ts">
import ButtonPadrao from '@/components/ButtonPadrao.vue';
import { mdiChartGantt, mdiDeleteVariant, mdiFilterOutline, mdiGroup, mdiHome, mdiInformationOutline } from '@mdi/js'

</script>

<template>

  <v-container class="about">
    <v-row>
      <v-col cols="12" sm="6" md="4">
        <v-card>
          <v-card-title>Inicio</v-card-title>
          <div class="d-flex flex-column align-center">
            <svg-icon type="mdi" :path="mdiHome" size="100" class="icones"></svg-icon>
          </div>
          <v-card-text class="d-flex justify-end">
            <RouterLink to="/home">
              <ButtonPadrao>
                Acessar
              </ButtonPadrao>
            </RouterLink>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" sm="6" md="4">
        <v-card color="gray">
          <v-card-title>Grupo de Lixeiras</v-card-title>
          <div class="d-flex flex-column align-center">
            <svg-icon type="mdi" :path="mdiGroup" size="100" class="icones"></svg-icon>
          </div>
          <v-card-text class="d-flex justify-end">
            <RouterLink to="/lixeiras">
              <ButtonPadrao>Acessar</ButtonPadrao>
            </RouterLink>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" sm="6" md="4">
        <v-card>
          <v-card-title>Lixeiras</v-card-title>
          <div class="d-flex flex-column align-center">
            <svg-icon type="mdi" :path="mdiDeleteVariant" size="100" class="icones"></svg-icon>
          </div>
          <v-card-text class="d-flex justify-end">
            <RouterLink to="/lixeiras">
              <ButtonPadrao>Acessar</ButtonPadrao>
            </RouterLink>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" sm="6" md="4">
        <v-card>
          <v-card-title>Filtros</v-card-title>
          <div class="d-flex flex-column align-center">
            <svg-icon type="mdi" :path="mdiFilterOutline" size="100" class="icones"></svg-icon>
          </div>
          <v-card-text class="d-flex justify-end">
            <RouterLink to="/lixeiras">
              <ButtonPadrao>Acessar</ButtonPadrao>
            </RouterLink>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" sm="6" md="4">
        <v-card>
          <v-card-title>Informar Nivel da Lixeira</v-card-title>
          <div class="d-flex flex-column align-center">
            <svg-icon type="mdi" :path="mdiInformationOutline" size="100" class="icones"></svg-icon>
          </div>
          <v-card-text class="d-flex justify-end">
            <RouterLink to="/informar-status-lixeira/1">
              <ButtonPadrao>Acessar</ButtonPadrao>
            </RouterLink>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" sm="6" md="4">
        <v-card>
          <v-card-title>Relatório Lixeira</v-card-title>
          <div class="d-flex flex-column align-center">
            <svg-icon type="mdi" :path="mdiChartGantt" size="100" class="icones"></svg-icon>
          </div>
          <v-card-text class="d-flex justify-end">
            <RouterLink to="/relatorio-lixeira">
              <ButtonPadrao>Acessar</ButtonPadrao>
            </RouterLink>
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

.icones {

  color: var(--btn-bg-primary-color);

}
</style>
