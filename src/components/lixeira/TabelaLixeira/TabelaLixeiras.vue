<script setup lang="js">

import { lixeira, selecionarLixeira, getEnderecosLixeiras } from '../lixeira.service.js'
import { mdiUpdate, mdiViewDashboardOutline } from '@mdi/js'
import BarraProgressoNivelLixeira from '../NivelLixeira/BarraProgressoNivelLixeira.vue'

const emit = defineEmits(['abrirModalExibirDetalhesLixeiraModal'])

const abrirModalExibirDetalhesLixeiraModal = (idLixeira) => {

    selecionarLixeira(idLixeira)
    emit("abrirModalExibirDetalhesLixeiraModal")

}


</script>
<template>

    <v-row justify="end">
        <v-btn color="rgb(94, 93, 93)" @click="getEnderecosLixeiras()">
            <svg-icon type="mdi" :path="mdiUpdate"></svg-icon>
        </v-btn>
    </v-row>

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
                    Capacidade Total(L)
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
                <td>{{ item.capacidade }}</td>
                <td><BarraProgressoNivelLixeira :item="item"></BarraProgressoNivelLixeira></td>
                <td>{{ item.data }}</td>
                <td>{{ item.hora }}</td>
                <td><v-btn color="rgb(94, 93, 93)" @click="abrirModalExibirDetalhesLixeiraModal(item.id)">
                        <svg-icon type="mdi" :path="mdiViewDashboardOutline"></svg-icon>
                        Visualizar
                    </v-btn></td>
            </tr>
        </tbody>
    </v-table>

</template>