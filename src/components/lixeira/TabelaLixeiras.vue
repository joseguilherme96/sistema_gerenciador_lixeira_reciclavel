<script setup lang="js">

import { lixeira } from './lixeira.service'

import { vCorNivelLixeira } from '../../directives/cor.nivel.lixeira.diretiva.js'


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
            </tr>
        </thead>
        <tbody>
            <tr v-for="item in lixeira" :key="item.name">
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
            </tr>
        </tbody>
    </v-table>

</template>