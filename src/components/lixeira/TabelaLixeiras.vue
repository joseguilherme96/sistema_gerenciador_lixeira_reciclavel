<script setup lang="js">

import { lixeira, selecionarLixeira } from './lixeira.service'

import { vCorNivelLixeira } from '../../directives/cor.nivel.lixeira.diretiva.js'
import { mdiViewDashboardOutline } from '@mdi/js'

const emit = defineEmits(['abrirModalExibirDetalhesLixeiraModal'])

const abrirModalExibirDetalhesLixeiraModal = (idLixeira) => {

    selecionarLixeira(idLixeira)
    emit("abrirModalExibirDetalhesLixeiraModal")

}


</script>
<template>

    <v-table>
        <thead>
            <tr>
                <th class="text-left">
                    ID Lixeira
                </th>
                <th class="text-left">
                    Endereço
                </th>
                <th class="text-left">
                    Cidade
                </th>
                <th class="text-left">
                    Estado
                </th>
                <th class="text-left">
                    Material Coletado Lixeira
                </th>
                <th class="text-left">
                    Capacidade(L)
                </th>
                <th class="text-left">
                    Nivel da Lixeira
                </th>
                <th class="text-left">
                    Data Atualização
                </th>
                <th class="text-left">
                    Hora Atualização
                </th>
                <th class="text-left">
                    Cor
                </th>
                <th class="text-left">
                    Ações
                </th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="item in lixeira" :key="item.name" @click="abrirModalExibirDetalhesLixeiraModal(item.id)">
                <td>{{ item.id }}</td>
                <td>{{ item.endereco }}</td>
                <td>{{ item.cidade }}</td>
                <td>{{ item.estado }}</td>
                <td>{{ item.materialColetado }}</td>
                <td>{{ item.capacidade }}</td>
                <td><v-progress-linear v-cor-nivel-lixeira="item.nivelLixeira" v-model:model-value="item.nivelLixeira"
                        :height="30">{{ item.nivelLixeira
                        }}%</v-progress-linear></td>
                <td>{{ item.data }}</td>
                <td>{{ item.hora }}</td>
                <td>{{ item.cor }}</td>
                <td><v-btn color="rgb(94, 93, 93)" @click="abrirModalExibirDetalhesLixeiraModal(item.id)">
                        <svg-icon type="mdi" :path="mdiViewDashboardOutline"></svg-icon>
                        Visualizar
                    </v-btn></td>
            </tr>
        </tbody>
    </v-table>

</template>