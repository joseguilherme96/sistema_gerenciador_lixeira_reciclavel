<script setup lang="js">

import { lixeira, selecionarGrupoLixeira, getGrupoLixeira } from '../lixeira.service.js'
import { mdiUpdate, mdiViewDashboardOutline } from '@mdi/js'
import BarraProgressoNivelLixeira from '../NivelLixeira/BarraProgressoNivelLixeira.vue'

const emit = defineEmits(['abrirModalGrupoLixeira'])

const abrirModalGrupoLixeira = async (grupoLixeiraId) => {

    await selecionarGrupoLixeira(grupoLixeiraId);

    emit("abrirModalGrupoLixeira")

}


</script>
<template>

    <v-row justify="end">
        <v-btn color="rgb(94, 93, 93)" @click="getGrupoLixeira()">
            <svg-icon type="mdi" :path="mdiUpdate"></svg-icon>
        </v-btn>
    </v-row>

    <v-table>
        <thead>
            <tr>
                <th class="text-left">
                    ID Grupo Lixeira
                </th>
                <th class="text-left">
                    Nome
                </th>
                <th class="text-left">
                    Descrição
                </th>
                <th class="text-left">
                    Endereço
                </th>
                <th class="text-left">
                    Bairro
                </th>
                <th class="text-left">
                    Cidade
                </th>
                <th class="text-left">
                    Estado
                </th>
                <th class="text-left">
                    Cep
                </th>
                <th class="text-left">
                    Capacidade Total(L)
                </th>
                <th class="text-left">
                    Nivel Total Lixeira
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
                <td>{{ item.nome }}</td>
                <td>{{ item.descricao }}</td>
                <td>{{ item.endereco }}</td>
                <td>{{ item.bairro }}</td>
                <td>{{ item.cidade }}</td>
                <td>{{ item.estado }}</td>
                <td>{{ item.cep }}</td>
                <td>{{ item.capacidade }}</td>
                <td>
                    <BarraProgressoNivelLixeira :item="item"></BarraProgressoNivelLixeira>
                </td>
                <td>{{ item.data }}</td>
                <td>{{ item.hora }}</td>
                <td><v-btn color="rgb(94, 93, 93)" @click="abrirModalGrupoLixeira(item.id_grupo_lixeira)">
                        <svg-icon type="mdi" :path="mdiViewDashboardOutline"></svg-icon>
                        Visualizar
                    </v-btn></td>
            </tr>
        </tbody>
    </v-table>

</template>