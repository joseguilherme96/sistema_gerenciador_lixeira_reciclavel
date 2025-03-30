<script setup lang="js">

import { lixeiraSelecionada } from '../lixeira.service.js'
import InformativoLixeira from '../InformativoLixeira/InformativoLixeira.vue';
import { computed, onMounted, ref, watch } from 'vue'
import BarraSuperior from '../BarraSuperior/BarraSuperior.vue';
import TituloPagina from '../Titulo/TituloPagina.vue';
import { mdiViewDashboardOutline } from '@mdi/js';
import DetalheLixeira from '../DetalheLixeira/DetalheLixeira.vue';

defineProps({
    data: Object
})

const configuracaoTitulo = ref({
    nome: 'Detalhes da Lixeira',
    icone: mdiViewDashboardOutline
})

const indexPaginaAtual = ref(0)

const lixeiraAtual = computed(() => {
    return lixeiraSelecionada.value.lixeiras[indexPaginaAtual.value]
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

                    <DetalheLixeira :lixeira="lixeira"></DetalheLixeira>

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