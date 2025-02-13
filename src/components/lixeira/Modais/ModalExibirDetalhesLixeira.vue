<script setup lang="js">

import { lixeiraSelecionada } from '../lixeira.service.js'
import InformativoLixeira from '../InformativoLixeira/InformativoLixeira.vue';
import QRCodeLixeira from '../QRCodeLixeira/QRCodeLixeira.vue'
import { baseUrl } from '../lixeira.service.js'
import { ref, watch } from 'vue'

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


</script>


<template>


    <v-dialog v-model="data.exibir" max-width="900">
        <template v-slot:default="{ isActive }">

            <v-card>

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
                </template>

            </v-card>
        </template>
    </v-dialog>

</template>