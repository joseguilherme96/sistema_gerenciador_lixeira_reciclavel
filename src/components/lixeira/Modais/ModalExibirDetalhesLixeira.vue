<script setup lang="js">

import { lixeiraSelecionada } from '../lixeira.service.js'
import InformativoLixeira from '../InformativoLixeira/InformativoLixeira.vue';
import QRCodeLixeira from '../QRCodeLixeira/QRCodeLixeira.vue'
import { baseUrl } from '../lixeira.service.js'
import { ref, watch } from 'vue'
import BarraSuperior from '../BarraSuperior/BarraSuperior.vue';
import TituloPagina from '../Titulo/TituloPagina.vue';
import { mdiViewDashboardOutline } from '@mdi/js';

defineProps({
    data: Object
})

const configuracaoQRCode = ref({
    width: 200,
    height: 200,
    valor: null
})


watch(() => lixeiraSelecionada.value, (newValue) => {


    configuracaoQRCode.value.valor = `${baseUrl}/informar-status-lixeira/${lixeiraSelecionada.value.id}`



})

const configuracaoTitulo = ref({
    nome: 'Detalhes da Lixeira',
    icone: mdiViewDashboardOutline
})

</script>


<template>


    <v-dialog v-model="data.exibir" max-width="900">
        <template v-slot:default="{ isActive }">

            <v-card>

                <BarraSuperior>

                    <template v-slot:titulo>

                        <TituloPagina :configuracaoTitulo="configuracaoTitulo"></TituloPagina>

                    </template>

                </BarraSuperior>

                <div class="d-flex flex-no-wrap justify-space-between">

                    <v-card>
                        <v-card-title>ID</v-card-title>
                        <v-card-subtitle>{{ lixeiraSelecionada.id }}</v-card-subtitle>
                        <v-card-title>Material Coletado</v-card-title>
                        <v-card-subtitle> {{ lixeiraSelecionada.materialColetado }}</v-card-subtitle>
                        <v-card-title>Capacidade(L)</v-card-title>
                        <v-card-subtitle>{{ lixeiraSelecionada.capacidade }}</v-card-subtitle>


                    </v-card>

                    <QRCodeLixeira v-if="lixeiraSelecionada.id" :configuracaoQRCode="configuracaoQRCode">
                    </QRCodeLixeira>

                </div>

                <InformativoLixeira></InformativoLixeira>

                <template v-slot:actions>
                    <v-btn variant="flat" color="rgb(94, 93, 93)" text="FECHAR" @click="data.exibir = false"></v-btn>
                    <RouterLink :to="`/informar-status-lixeira/${lixeiraSelecionada.id}`" v-if="lixeiraSelecionada.id">
                        <v-btn variant="flat" color="rgb(94, 93, 93)" text="INFORMAR STATUS LIXEIRA"></v-btn>
                    </RouterLink>
                </template>

            </v-card>
        </template>
    </v-dialog>

</template>