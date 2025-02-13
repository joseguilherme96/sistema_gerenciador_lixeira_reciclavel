<script setup lang="js">

import { lixeiraSelecionada } from '../lixeira.service.js'
import InformativoLixeira from '../InformativoLixeira/InformativoLixeira.vue';


defineProps({
    data: Object
})


</script>

<template>


    <v-dialog v-model="data.exibir" max-width="900">
        <template v-slot:default="{ isActive }">
            
            <v-card>
                <v-card>

                    <v-card-title>ID</v-card-title>
                    <v-card-subtitle>{{ lixeiraSelecionada.id }}</v-card-subtitle>
                    <v-card-title>Material Coletado</v-card-title>
                    <v-card-subtitle> {{ lixeiraSelecionada.materialColetado }}</v-card-subtitle>
                    <v-card-title>Capacidade(L)</v-card-title>
                    <v-card-subtitle>{{ lixeiraSelecionada.capacidade }}</v-card-subtitle>

                </v-card>

                <InformativoLixeira></InformativoLixeira>

                <template v-slot:actions>
                    <v-btn variant="flat"  color="rgb(94, 93, 93)" text="FECHAR" @click="data.exibir = false"></v-btn>
                </template>

            </v-card>
        </template>
    </v-dialog>

</template>