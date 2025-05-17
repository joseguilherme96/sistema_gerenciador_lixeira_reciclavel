<script setup lang="js">

// Vue
import { onMounted, ref, watch } from 'vue'
import { storeToRefs } from 'pinia';

// Componentes
import InformativoLixeira from '../InformativoLixeira/InformativoLixeira.vue';
import BarraSuperior from '../BarraSuperior/BarraSuperior.vue';
import TituloPagina from '../Titulo/TituloPagina.vue';
import { mdiViewDashboardOutline, mdiTrashCan, mdiOpenInApp, mdiCloseBox, mdiDeleteEmpty, mdiDelete } from '@mdi/js';
import DetalheLixeira from '../DetalheLixeira/DetalheLixeira.vue';

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

</script>


<template>


    <v-dialog v-model="data.exibir" max-width="900">
        <template v-slot:default="{ isActive }">

            <v-card>

                <BarraSuperior>

                    <template v-slot:titulo>

                        <TituloPagina :configuracaoTitulo="configuracaoTitulo">
                        </TituloPagina>
                        <v-chip :color="lixeira.esta_aberta == 'Aberta' ? 'brown' : 'green'">
                            <svg-icon type="mdi"
                                :path="lixeira.esta_aberta == 'Aberta' ? mdiDeleteEmpty : mdiDelete"></svg-icon>
                            {{
                                lixeira.esta_aberta }}</v-chip>


                    </template>

                </BarraSuperior>

                <v-card class="mt-5" style="overflow: scroll;">

                    <DetalheLixeira :lixeira="lixeira"></DetalheLixeira>

                    <InformativoLixeira></InformativoLixeira>

                    <template v-slot:actions>
                        <div class="d-flex justify-end" style="width: 100%;">
                            <v-btn variant="flat" color="rgb(94, 93, 93)" text="ANTERIOR" @click="voltarPagina"
                                class="ml-1"></v-btn>
                            <v-btn variant="flat" color="rgb(94, 93, 93)" text="PRÓXIMO" @click="avancarPagina"
                                class="ml-1"></v-btn>
                            <v-btn variant="flat" color="rgb(94, 93, 93)" text="FECHAR" @click="data.exibir = false"
                                class="ml-1"></v-btn>
                            <RouterLink :to="`/informar-status-lixeira/${lixeira.id_lixeira}`"
                                v-if="lixeira.id_lixeira">
                                <v-btn variant="flat" color="rgb(94, 93, 93)" text="INFORMAR STATUS LIXEIRA"
                                    class="ml-1"></v-btn>
                            </RouterLink>
                        </div>
                    </template>

                </v-card>

            </v-card>
        </template>
    </v-dialog>

</template>