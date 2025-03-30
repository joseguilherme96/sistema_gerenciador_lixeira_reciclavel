<script setup lang="js">

import { form } from '../lixeira.service.js'
import { corLixeira } from '../cor.lixeira.service.js'
import { materiaisReciclaveis } from '../materiais.reciclaveis.services.js'
import { niveisLixeira } from '../nivel.lixeira.service.js'
import BarraSuperior from '../BarraSuperior/BarraSuperior.vue'
import { cidades, estados } from '../../../services/endereco.service.js'
import TituloPagina from '../Titulo/TituloPagina.vue'
import { mdiAccount, mdiAccountPlus, mdiDatabase, mdiPlus, mdiTruck } from '@mdi/js'
import { ref } from 'vue'

const configuracaoTitulo = {

    nome: 'Cadastro Local Lixeira',
    icone: mdiAccountPlus

}

const configuracaoTitulo1 = {
    nome: 'Cadastro de Lixeiras Neste Local',
    icone: mdiAccountPlus
}

const quantidadeLixeira = ref(1)

const ocultarBotaoAdicionarLixeira = (index) => {

    form.value.lixeiras[index].exibirBotaoAdicionarLixeira = false

}

const criarEspacoParaArmazenamentoDaLixeira = () => {

    ocultarBotaoAdicionarLixeira(quantidadeLixeira.value - 1);

    quantidadeLixeira.value++
    form.value.lixeiras.push({ exibirBotaoAdicionarLixeira: true })


}

</script>

<template>
    <v-container>
        <BarraSuperior>

            <template v-slot:titulo>
                <TituloPagina :configuracaoTitulo="configuracaoTitulo"></TituloPagina>
            </template>

        </BarraSuperior>

        <v-row>

            <v-col cols="4" sm="12">
                <v-text-field label="Cep" v-model="form.cep" :maxlength="9"></v-text-field>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="4" sm="6">
                <v-text-field label="Endereço" v-model="form.endereco"></v-text-field>
            </v-col>
            <v-col cols="4" sm="6">
                <v-text-field label="Bairro" v-model="form.bairro"></v-text-field>
            </v-col>
            <v-col cols="4" sm="4">
                <v-select label="Cidade" :items="cidades" v-model="form.cidade"></v-select>
            </v-col>
            <v-col cols="4" sm="4">
                <v-select label="Estado" :items="estados" v-model="form.estado"></v-select>
            </v-col>
        </v-row>

        <BarraSuperior>

            <template v-slot:titulo>
                <TituloPagina :configuracaoTitulo="configuracaoTitulo1"></TituloPagina>
            </template>

        </BarraSuperior>

        <v-card v-for="(lixeira, index) in form.lixeiras" class="pl-5 pr-5 mt-10">
            <v-card-subtitle>
                Lixeira {{ index + 1 }}
            </v-card-subtitle>
            <v-row>
                <v-col cols="4" sm="8" class="m-4">
                    <v-text-field label="Descricao" v-model="lixeira.descricaoLixeira"></v-text-field>
                </v-col>
                <v-col cols="4" sm="4">
                    <v-select label="Material Coletado" :items="materiaisReciclaveis"
                        v-model="lixeira.materialColetado"></v-select>
                </v-col>
                <v-col cols="4" sm="4">
                    <v-text-field label="Capacidade(L)" type="number" v-model="lixeira.capacidade"></v-text-field>
                </v-col>
                <v-col cols="4" sm="4">
                    <v-select label="Nivel Lixeira" :items="niveisLixeira" v-model="lixeira.nivelLixeira"></v-select>
                </v-col>
                <v-col cols="12" sm="12">
                    <v-select label="Cor" :items="corLixeira" v-model="lixeira.cor"></v-select>
                </v-col>
                <v-col cols="4" sm="12">
                    <v-text-field label="Observação" v-model="lixeira.observacao"></v-text-field>
                </v-col>
                <v-container class="d-flex justify-end">
                    <v-btn color="rgb(94, 93, 93)" @click="criarEspacoParaArmazenamentoDaLixeira()"
                        v-if="lixeira.exibirBotaoAdicionarLixeira">
                        <svg-icon type="mdi" :path="mdiPlus"></svg-icon>
                        Adicionar mais lixeiras
                    </v-btn>
                </v-container>

            </v-row>
        </v-card>

    </v-container>

</template>