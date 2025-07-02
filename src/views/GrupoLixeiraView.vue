<script setup lang="js">

// Vue
import { onMounted, ref } from 'vue'
import { storeToRefs } from 'pinia';

// Componentes
import BarraSuperior from '../components/lixeira/BarraSuperior/BarraSuperior.vue';
import FiltroPesquisa from '@/components/lixeira/FIltroPesquisaLixeira/FiltroPesquisa.vue';
import TabelaGrupoLixeira from '../components/lixeira/TabelaLixeira/TabelaGrupoLixeira.vue';
import ModalCadastro from '../components/lixeira/Modais/ModalCadastro.vue'
import ModalExibirDetalhesLixeirasDoGrupo from '../components/lixeira/Modais/ModalExibirDetalhesLixeirasDoGrupo.vue'
import TituloPagina from '../components/lixeira/Titulo/TituloPagina.vue';

//Icones
import { mdiMagnify, mdiPlus, mdiTruck } from '@mdi/js'

//Serviços
import { getCidades, getEstados } from '../services/endereco.service.js'

// Gerenciadores de Estado
import { useEstadoStore } from '@/stores/estado.js'
import { useCidadeStore } from '@/stores/cidade.js'
import { useFiltroGrupoLixeiraStore } from '@/stores/filtro.js'
import { useMaterialReciclavelStore } from '@/stores/MaterialReciclavel.js'
import ButtonPadrao from '@/components/ButtonPadrao.vue';

const { filtroEstaAberto } = storeToRefs(useFiltroGrupoLixeiraStore())
const useMaterialReciclavel = useMaterialReciclavelStore();


onMounted(() => {

    getEstados(useEstadoStore);
    getCidades(useCidadeStore);
    useMaterialReciclavel.getMaterialReciclavel()

})


const modalCadastroLixeira = ref({
    titulo: 'Cadastro de Lixeira',
    exibir: false
})

const modalDetalhesGrupoLixeira = ref({

    titulo: 'Detalhes Lixeira',
    exibir: false


})

function abrirFiltro() {
    filtroEstaAberto.value = !filtroEstaAberto.value
}

function abrirModalCadastroLixeira() {
    modalCadastroLixeira.value.exibir = true
}

function abrirModalLixeira() {

    modalDetalhesGrupoLixeira.value.exibir = true;

}

const configuracaoTitulo = ref({
    nome: 'Acompanhamento do nível das lixeiras por grupo',
    icone: mdiTruck
})

</script>

<template>

    <BarraSuperior style="background-color: var(--btn-bg-secondary-color)">
        <template v-slot:titulo>
            <TituloPagina :configuracaoTitulo="configuracaoTitulo"></TituloPagina>
        </template>
        <template v-slot:opcoes>
            <ButtonPadrao @click="abrirModalCadastroLixeira()" class="mr-5">
                <svg-icon type="mdi" :path="mdiPlus"></svg-icon>
                Cadastrar Grupo Lixeira / Lixeira
            </ButtonPadrao>
            <ButtonPadrao @click="abrirFiltro()">
                <svg-icon type="mdi" :path="mdiMagnify"></svg-icon>
                Filtro Lixeiras
            </ButtonPadrao>
        </template>
    </BarraSuperior>
    <FiltroPesquisa v-if="filtroEstaAberto"></FiltroPesquisa>


    <TabelaGrupoLixeira @abrirModalLixeirasDoGrupoLixeiraSelecionado="abrirModalLixeira">
    </TabelaGrupoLixeira>

    <ModalCadastro :data="modalCadastroLixeira"></ModalCadastro>
    <ModalExibirDetalhesLixeirasDoGrupo :data="modalDetalhesGrupoLixeira" v-if="modalDetalhesGrupoLixeira.exibir">
    </ModalExibirDetalhesLixeirasDoGrupo>
</template>
