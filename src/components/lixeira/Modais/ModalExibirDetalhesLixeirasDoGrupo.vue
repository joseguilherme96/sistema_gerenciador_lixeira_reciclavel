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
import ButtonPadrao from '@/components/ButtonPadrao.vue';

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

                <BarraSuperior style="background-color: var(--btn-bg-primary-color)">

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
                    <v-row class="d-flex justify-end mt-5 mb-5 mr-5" style="width: 100%;">
                        <ButtonPadrao v-if="!exibirGrafico" color="rgb(94, 93, 93)" @click="voltarPagina" class="ml-1">
                            ANTERIOR
                        </ButtonPadrao>
                        <ButtonPadrao v-if="!exibirGrafico" @click="avancarPagina" class="ml-1">PRÓXIMO</ButtonPadrao>
                        <ButtonPadrao v-if="!exibirGrafico" @click="data.exibir = false" class="ml-1">FECHAR
                        </ButtonPadrao>
                        <RouterLink :to="`/informar-status-lixeira/${lixeira.id_lixeira}`"
                            v-if="lixeira.id_lixeira && !exibirGrafico">
                            <ButtonPadrao class="ml-1">INFORMATIVO LIXEIRA</ButtonPadrao>
                        </RouterLink>
                        <ButtonPadrao class="ml-1" @click="abrirGrafico()" v-if="!exibirGrafico">
                            VISUALIZAR GRÁfiCO
                        </ButtonPadrao>
                        <ButtonPadrao class="ml-1" @click="exibirGrafico = false" v-else>FECHAR GRÁFICO
                        </ButtonPadrao>
                    </v-row>
                </template>

            </v-card>
        </template>
    </v-dialog>

</template>