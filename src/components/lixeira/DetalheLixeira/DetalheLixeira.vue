<script setup lang="js">

import { ref, watchEffect } from 'vue';
import BarraProgressoNivelLixeira from '../NivelLixeira/BarraProgressoNivelLixeira.vue';
import QRCodeLixeira from '../QRCodeLixeira/QRCodeLixeira.vue';
import { baseUrl } from '../lixeira.service.js'

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
    props.lixeira.configuracaoQRCode.valor = `${baseUrl}/lixeira/${props.lixeira.id}`

}


watchEffect(() => {

    gerarValorQRCode();

})


</script>
<template>

    <div class="d-flex flex-no-wrap justify-space-between">
        <div>
            <v-card-title>ID</v-card-title>
            <v-card-subtitle>{{ lixeira.id }}</v-card-subtitle>
            <v-card-title>Descrição</v-card-title>
            <v-card-subtitle>{{ lixeira.descricaoLixeira }}</v-card-subtitle>
            <v-card-title>Material Coletado</v-card-title>
            <v-card-subtitle> {{ lixeira.materialColetado }}</v-card-subtitle>

        </div>
        <div>

            <v-card-title>Capacidade(L)</v-card-title>
            <v-card-subtitle>{{ lixeira.capacidade }}</v-card-subtitle>
            <v-card-title>Nivel Lixeira</v-card-title>
            <v-card-subtitle>
                <BarraProgressoNivelLixeira :item="lixeira"></BarraProgressoNivelLixeira>
            </v-card-subtitle>
        </div>
        <div>
            <QRCodeLixeira :configuracaoQRCode="lixeira.configuracaoQRCode" v-if="lixeira.configuracaoQRCode">
            </QRCodeLixeira>
        </div>
    </div>

</template>