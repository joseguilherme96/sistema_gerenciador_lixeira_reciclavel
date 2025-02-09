<script setup lang="js">

import BarraSuperior from '@/components/lixeira/BarraSuperior.vue';
import { getLixeiras, limparCampos, criarLixeira } from '../components/lixeira/lixeira.service'
import { onMounted, ref } from 'vue'
import FiltroPesquisa from '@/components/lixeira/FiltroPesquisa.vue';
import TabelaLixeiras from '@/components/lixeira/TabelaLixeiras.vue';
import ModalCadastro from '../components/modal/ModalCadastro.vue'
import FormularioCadastroLixeira from '../components/lixeira/FormularioCadastroLixeira.vue'
import { mdiMagnify, mdiPlus } from '@mdi/js'
import { getCidades, getEstados } from '../services/endereco.service.js'

onMounted(() => {
    getLixeiras();
})

getEstados();
getCidades();

const dados = ref({
    titulo: 'Cadastro de Lixeira',
    nome: '',
    localizacao: '',
    capacidade: '',
    tipo: '',
    nivelLixeira: '',
    observacao: '',
    exibir: false
})
const filtroEstaAberto = ref(false)

function abrirFiltro() {
    filtroEstaAberto.value = !filtroEstaAberto.value
}

function abrirModalCadastroLixeira() {
    dados.value.exibir = true
}

function cadastrarLixeira() {
    criarLixeira().then((res) => {

        getLixeiras();

        console.log(res);
        dados.value.exibir = false
    })
}

</script>

<template>
    <v-container>
        <ModalCadastro :data="dados">
            <template v-slot:conteudo>

                <FormularioCadastroLixeira></FormularioCadastroLixeira>

            </template>
            <template v-slot:botoes>
                <v-btn variant="flat" color="rgb(94, 93, 93)" @click="limparCampos()">
                    Limpar Campos
                </v-btn>
                <v-btn variant="flat" color="rgb(94, 93, 93)" text="CADASTRAR LIXEIRA"
                    @click="cadastrarLixeira()"></v-btn>
                <v-btn variant="flat" color="rgb(94, 93, 93)" text="Fechar" @click="dados.exibir = false"></v-btn>
            </template>

        </ModalCadastro>

        <BarraSuperior>
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
    </v-container>
    <TabelaLixeiras></TabelaLixeiras>
</template>
