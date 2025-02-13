<script setup lang="js">

import BarraSuperior from '../components/lixeira/BarraSuperior/BarraSuperior.vue';
import { getLixeiras } from '../components/lixeira/lixeira.service.js'
import { onMounted, ref } from 'vue'
import FiltroPesquisa from '@/components/lixeira/FIltroPesquisaLixeira/FiltroPesquisa.vue';
import TabelaLixeiras from '@/components/lixeira/TabelaLixeira/TabelaLixeiras.vue';
import ModalCadastro from '../components/lixeira/Modais/ModalCadastro.vue'
import { mdiMagnify, mdiPlus, mdiTrashCan, mdiTruck } from '@mdi/js'
import { getCidades, getEstados } from '../services/endereco.service.js'
import ModalExibirDetalhesLixeira from '../components/lixeira/Modais/ModalExibirDetalhesLixeira.vue'
import TituloPagina from '../components/lixeira/Titulo/TituloPagina.vue';

onMounted(() => {
    getLixeiras();
})

getEstados();
getCidades();

const modalCadastroLixeira = ref({
    titulo: 'Cadastro de Lixeira',
    exibir: false
})

const modalDetalhesLixeira = ref({

    titulo: 'Detalhes Lixeira',
    exibir: false


})
const filtroEstaAberto = ref(false)

function abrirFiltro() {
    filtroEstaAberto.value = !filtroEstaAberto.value
}

function abrirModalCadastroLixeira() {
    modalCadastroLixeira.value.exibir = true
}

function abrirModalExibirDetalhesLixeiraModal() {

    modalDetalhesLixeira.value.exibir = true;

}

const configuracaoTitulo = ref({
    nome: 'Acompanhamento do Nível das Lixeiras',
    icone: mdiTruck
})

</script>

<template>

    <BarraSuperior>
        <template v-slot:titulo>
            <TituloPagina :configuracaoTitulo="configuracaoTitulo"></TituloPagina>
        </template>
        <template v-slot:opcoes>
            <v-btn color="primary" @click="abrirModalCadastroLixeira()">
                <svg-icon type="mdi" :path="mdiPlus"></svg-icon>
                Cadastrar Lixeira
            </v-btn>
            <v-btn color="primary" @click="abrirFiltro()">
                <svg-icon type="mdi" :path="mdiMagnify"></svg-icon>
                Filtro Lixeiras
            </v-btn>
        </template>
    </BarraSuperior>
    <FiltroPesquisa v-if="filtroEstaAberto"></FiltroPesquisa>


    <TabelaLixeiras @abrirModalExibirDetalhesLixeiraModal="abrirModalExibirDetalhesLixeiraModal"></TabelaLixeiras>

    <ModalCadastro :data="modalCadastroLixeira"></ModalCadastro>
    <ModalExibirDetalhesLixeira :data="modalDetalhesLixeira"></ModalExibirDetalhesLixeira>
</template>
