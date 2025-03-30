<script setup lang="js">

import { lixeiraSelecionada } from '../lixeira.service.js'
import InformativoLixeira from '../InformativoLixeira/InformativoLixeira.vue';
import QRCodeLixeira from '../QRCodeLixeira/QRCodeLixeira.vue'
import { baseUrl } from '../lixeira.service.js'
import { computed, ref, watch } from 'vue'
import BarraSuperior from '../BarraSuperior/BarraSuperior.vue';
import TituloPagina from '../Titulo/TituloPagina.vue';
import { mdiViewDashboardOutline } from '@mdi/js';

import BarraProgressoNivelLixeira from '../NivelLixeira/BarraProgressoNivelLixeira.vue';

defineProps({
    data: Object
})

const configuracaoTitulo = ref({
    nome: 'Detalhes da Lixeira',
    icone: mdiViewDashboardOutline
})

const indexPaginaAtual = ref(0)


const configuracaoQRCode = ref({
    width: 200,
    height: 200,
    valor: null

})

const lixeiraAtual = computed(() => {
    return lixeiraSelecionada.value.lixeiras[indexPaginaAtual.value]
})

const gerarUrlParaQRCode = ()=>{

    configuracaoQRCode.value.valor = `${baseUrl}/lixeira/${lixeiraSelecionada.value.lixeiras[indexPaginaAtual.value].id}`
}


watch(() => indexPaginaAtual.value, () => {


    gerarUrlParaQRCode();

})

const avancarPagina = () => {

    if (indexPaginaAtual.value < lixeiraSelecionada.value.lixeiras.length - 1) {
        indexPaginaAtual.value++
    }
}

const voltarPagina = () => {

    if (indexPaginaAtual.value > 0) {
        indexPaginaAtual.value--
    }
}


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

                <v-card v-for="(lixeira, index) in lixeiraSelecionada.lixeiras" class="mt-5"
                    v-show="indexPaginaAtual == index">


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
                            <QRCodeLixeira :configuracaoQRCode="configuracaoQRCode" v-if="indexPaginaAtual == index">
                            </QRCodeLixeira>
                        </div>
                    </div>

                    <InformativoLixeira :lixeiraSelecionada="lixeiraAtual"></InformativoLixeira>

                    <template v-slot:actions>
                        <v-btn variant="flat" color="rgb(94, 93, 93)" text="ANTERIOR" @click="voltarPagina"></v-btn>
                        <v-btn variant="flat" color="rgb(94, 93, 93)" text="PRÓXIMO" @click="avancarPagina"></v-btn>
                        <v-btn variant="flat" color="rgb(94, 93, 93)" text="FECHAR"
                            @click="data.exibir = false"></v-btn>
                        <RouterLink :to="`/informar-status-lixeira/${lixeira.id}`" v-if="lixeira.id" target="_blank">
                            <v-btn variant="flat" color="rgb(94, 93, 93)" text="INFORMAR STATUS LIXEIRA"></v-btn>
                        </RouterLink>
                    </template>

                </v-card>

            </v-card>
        </template>
    </v-dialog>

</template>