<script setup lang="js">

import { lixeira, selecionarLixeira, getEnderecosLixeiras, getLixeirasQuery, lixeiraSelecionada } from '../lixeira.service.js'
import { mdiUpdate, mdiViewDashboardOutline } from '@mdi/js'
import BarraProgressoNivelLixeira from '../NivelLixeira/BarraProgressoNivelLixeira.vue'

const emit = defineEmits(['abrirModalExibirDetalhesLixeiraModal'])

const abrirModalExibirDetalhesLixeiraModal = async (idLixeira) => {

    await selecionarLixeira(idLixeira);

    await getLixeirasQuery({ grupo_lixeira_id: idLixeira }).then((response) => {

        if (response.length == 0) {

            return;

        }

        lixeiraSelecionada.value.lixeiras = response


    })

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
            <tr v-for="item in lixeira" :key="item.name">
                <td>{{ item.id_grupo_lixeira }}</td>
                <td>{{ item.endereco }}</td>
                <td>{{ item.cidade }}</td>
                <td>{{ item.estado }}</td>
                <td>{{ item.capacidade }}</td>
                <td>
                    <BarraProgressoNivelLixeira :item="item"></BarraProgressoNivelLixeira>
                </td>
                <td>{{ item.data }}</td>
                <td>{{ item.hora }}</td>
                <td><v-btn color="rgb(94, 93, 93)" @click="abrirModalExibirDetalhesLixeiraModal(item.id_grupo_lixeira)">
                        <svg-icon type="mdi" :path="mdiViewDashboardOutline"></svg-icon>
                        Visualizar
                    </v-btn></td>
            </tr>
        </tbody>
    </v-table>

</template>