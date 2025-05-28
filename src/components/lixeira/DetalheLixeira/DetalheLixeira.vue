<script setup lang="js">

import { ref, watchEffect } from 'vue';
import BarraProgressoNivelLixeira from '../NivelLixeira/BarraProgressoNivelLixeira.vue';
import QRCodeLixeira from '../QRCodeLixeira/QRCodeLixeira.vue';

const baseUrl = import.meta.env.VITE_APP_BASE_URL

const props = defineProps({
    lixeira: Object
})

const configuracaoQRCode = ref({
    width: 200,
    height: 200,
    valor: null

})

function gerarValorQRCode() {

    props.lixeira.configuracaoQRCode = configuracaoQRCode.value;
    props.lixeira.configuracaoQRCode.valor = `${baseUrl}/lixeira/${props.lixeira.id_lixeira}`

}


watchEffect(() => {

    gerarValorQRCode();

})


</script>
<template>

    <v-row class="d-flex flex-no-wrap justify-space-between">
        <v-col cols="6" sm="4">
            <v-card-title>Grupo ID</v-card-title>
            <v-card-subtitle>{{ lixeira.grupo_lixeira_id }}</v-card-subtitle>
            <v-card-title>ID Lixeira</v-card-title>
            <v-card-subtitle>{{ lixeira.id_lixeira }}</v-card-subtitle>
            <v-card-title>Descrição</v-card-title>
            <v-card-subtitle>{{ lixeira.observacao }}</v-card-subtitle>

        </v-col>
        <v-col cols="6" sm="4">
            <v-card-title>Material Coletado</v-card-title>
            <v-card-subtitle> {{ lixeira.mat_colet_id }}</v-card-subtitle>
            <v-card-title>Capacidade(L)</v-card-title>
            <v-card-subtitle>{{ lixeira.capacidade }}</v-card-subtitle>
            <v-card-title>Nivel Lixeira</v-card-title>
            <v-card-subtitle>
                <BarraProgressoNivelLixeira :item="lixeira"></BarraProgressoNivelLixeira>
            </v-card-subtitle>

        </v-col>

        <v-col cols="12" sm="4">
            <v-row class="justify-center">
                <v-card-title>Ponto Lixo ID</v-card-title>
                <v-card-subtitle> {{ lixeira.ponto_lixo_id }}</v-card-subtitle>
                <QRCodeLixeira :configuracaoQRCode="lixeira.configuracaoQRCode" v-if="lixeira.configuracaoQRCode">
                </QRCodeLixeira>

            </v-row>
        </v-col>
    </v-row>

</template>