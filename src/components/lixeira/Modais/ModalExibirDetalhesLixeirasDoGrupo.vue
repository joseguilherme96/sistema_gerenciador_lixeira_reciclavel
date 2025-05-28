<script setup lang="js">

// Vue
import { onMounted, ref, watch } from 'vue'
import { storeToRefs } from 'pinia';

// Componentes
import InformativoLixeira from '../InformativoLixeira/InformativoLixeira.vue';
import BarraSuperior from '../BarraSuperior/BarraSuperior.vue';
import TituloPagina from '../Titulo/TituloPagina.vue';
import { mdiViewDashboardOutline, mdiDeleteEmpty, mdiDelete } from '@mdi/js';
import DetalheLixeira from '../DetalheLixeira/DetalheLixeira.vue';
import GraficoEvolucaoNivelLixo from '../GraficoLixeira/GraficoEvolucaoNivelLixo.vue'
import VChipLixeiraEstaAberta from '../VChips/VChipLixeiraEstaAberta.vue'

//Serviços
import { getInformativoLixeiraPorPontoLixoId } from '../../../services/informativo.lixeira.service.js'

//Gerenciadores de estado
import { useInformativoLixeiraStore } from '@/stores/informativoLixeira'
import { useLixeiraStore } from '@/stores/lixeira'

const { listaLixeira, setLixeira } = useLixeiraStore()
const { lixeira } = storeToRefs(useLixeiraStore())


defineProps({
    data: Object
})


const indexPaginaAtual = ref(0)

const configuracaoTitulo = ref({
    nome: `Detalhe Grupo Lixeira`,
    icone: mdiViewDashboardOutline,
    lixeiraEstaAberta: lixeira.value.esta_aberta
})

const configuracaoTituloGrafico = ref({
    nome: `Gráfico`,
    icone: mdiViewDashboardOutline,
    lixeiraEstaAberta: lixeira.value.esta_aberta
})

const atualizarPaginacaoNoTitulo = () => {
    const paginacao = `${indexPaginaAtual.value + 1}/${listaLixeira.length}`
    configuracaoTitulo.value.nome = `Detalhe Grupo Lixeira ${paginacao}`
}

const getInformativo = async () => {

    await getInformativoLixeiraPorPontoLixoId(useInformativoLixeiraStore, listaLixeira[indexPaginaAtual.value].ponto_lixo_id);

}

const avancarPagina = () => {

    if (indexPaginaAtual.value < listaLixeira.length - 1) {
        indexPaginaAtual.value++

        atualizarPaginacaoNoTitulo();
        getInformativo();
    }
}

const voltarPagina = () => {

    if (indexPaginaAtual.value > 0) {
        indexPaginaAtual.value--

        atualizarPaginacaoNoTitulo();
        getInformativo();
    }
}

onMounted(() => {
    atualizarPaginacaoNoTitulo();
    getInformativo();
    setLixeira(listaLixeira[0])
})

watch(() => indexPaginaAtual.value, (index) => {

    setLixeira(listaLixeira[index])

})

let exibirGrafico = ref(false)

const abrirGrafico = () => {

    exibirGrafico.value = true
}

</script>


<template>


    <v-dialog v-model="data.exibir" max-width="900">
        <template v-slot:default="{ isActive }">

            <v-card>

                <BarraSuperior>

                    <template v-slot:titulo>

                        <TituloPagina
                            :configuracaoTitulo="!exibirGrafico ? configuracaoTitulo : configuracaoTituloGrafico">
                        </TituloPagina>
                        <VChipLixeiraEstaAberta></VChipLixeiraEstaAberta>


                    </template>

                </BarraSuperior>

                <div v-if="!exibirGrafico">

                    <DetalheLixeira :lixeira="lixeira" v-if="!exibirGrafico"></DetalheLixeira>

                    <v-card class="mt-5" style="overflow: scroll;">

                        <InformativoLixeira v-if="!exibirGrafico"></InformativoLixeira>

                    </v-card>
                </div>


                <div v-if="exibirGrafico">

                    <GraficoEvolucaoNivelLixo></GraficoEvolucaoNivelLixo>

                </div>

                <template v-slot:actions>
                    <v-row class="d-flex justify-center" style="width: 100%;">
                        <v-col cols="4" sm="2" v-if="!exibirGrafico">
                            <v-btn variant="flat" color="rgb(94, 93, 93)" text="ANTERIOR" @click="voltarPagina"
                                class="ml-1"></v-btn>
                        </v-col>
                        <v-col cols="4" sm="2" v-if="!exibirGrafico">
                            <v-btn variant="flat" color="rgb(94, 93, 93)" text="PRÓXIMO" @click="avancarPagina"
                                class="ml-1"></v-btn>
                        </v-col>
                        <v-col cols="3" sm="2" v-if="!exibirGrafico">
                            <v-btn variant="flat" color="rgb(94, 93, 93)" text="FECHAR" @click="data.exibir = false"
                                class="ml-1"></v-btn>
                        </v-col>
                        <v-col sm="12">
                            <v-row class="justify-end">
                                <v-col cols="8" sm="4">
                                    <RouterLink :to="`/informar-status-lixeira/${lixeira.id_lixeira}`"
                                        v-if="lixeira.id_lixeira">
                                        <v-btn variant="flat" color="rgb(94, 93, 93)" text="INFORMAR STATUS LIXEIRA"
                                            class="ml-1"></v-btn>
                                    </RouterLink>
                                </v-col>
                                <v-col cols="7" sm="3">
                                    <v-btn variant="flat" color="rgb(94, 93, 93)" class="ml-1" text="VISUALIZAR GRÁfiCO"
                                        @click="abrirGrafico()" v-if="!exibirGrafico"></v-btn>

                                    <v-btn variant="flat" color="rgb(94, 93, 93)" class="ml-1" text="FECHAR GRÁFICO"
                                        @click="exibirGrafico = false" v-else></v-btn>
                                </v-col>
                            </v-row>
                        </v-col>
                    </v-row>
                </template>

            </v-card>
        </template>
    </v-dialog>

</template>