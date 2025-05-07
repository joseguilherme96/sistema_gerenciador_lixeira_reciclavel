<script setup lang="js">

// Vue
import { onMounted, ref } from 'vue'

// Componentes
import BarraSuperior from '../components/lixeira/BarraSuperior/BarraSuperior.vue';
import FiltroPesquisa from '@/components/lixeira/FIltroPesquisaLixeira/FiltroPesquisa.vue';
import TabelaGrupoLixeira from '../components/lixeira/TabelaLixeira/TabelaGrupoLixeira.vue';
import ModalCadastro from '../components/lixeira/Modais/ModalCadastro.vue'
import ModalExibirDetalhesGrupoLixeira from '../components/lixeira/Modais/ModalExibirDetalhesGrupoLixeira.vue'
import TituloPagina from '../components/lixeira/Titulo/TituloPagina.vue';

//Icones
import { mdiMagnify, mdiPlus, mdiTruck } from '@mdi/js'

//Serviços
import { getCidades, getEstados } from '../services/endereco.service.js'

// Gerenciadores de Estado
import { useEstadoStore } from '@/stores/estado.js'
import { useCidadeStore } from '@/stores/cidade.js'

onMounted(() => {

    getEstados(useEstadoStore);
    getCidades(useCidadeStore);

})


const modalCadastroLixeira = ref({
    titulo: 'Cadastro de Lixeira',
    exibir: false
})

const modalDetalhesGrupoLixeira = ref({

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

function abrirModalLixeira() {

    modalDetalhesGrupoLixeira.value.exibir = true;

}

const configuracaoTitulo = ref({
    nome: 'Acompanhamento do nível das lixeiras por grupo',
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
                Cadastrar Grupo Lixeira / Lixeira
            </v-btn>
            <v-btn color="primary" @click="abrirFiltro()">
                <svg-icon type="mdi" :path="mdiMagnify"></svg-icon>
                Filtro Lixeiras
            </v-btn>
        </template>
    </BarraSuperior>
    <FiltroPesquisa v-if="filtroEstaAberto"></FiltroPesquisa>


    <TabelaGrupoLixeira @abrirModalLixeirasDoGrupoLixeiraSelecionado="abrirModalLixeira">
    </TabelaGrupoLixeira>

    <ModalCadastro :data="modalCadastroLixeira"></ModalCadastro>
    <ModalExibirDetalhesGrupoLixeira :data="modalDetalhesGrupoLixeira" v-if="modalDetalhesGrupoLixeira.exibir">
    </ModalExibirDetalhesGrupoLixeira>
</template>
