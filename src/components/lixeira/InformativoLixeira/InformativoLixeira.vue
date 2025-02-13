<script setup lang="js">

import { lixeiraSelecionada } from '../lixeira.service.js'
import { informativoLixeira, getInformativoLixeiraPorIdLixeira } from './informativo.lixeira.service.js'

getInformativoLixeiraPorIdLixeira(lixeiraSelecionada.value.id);

</script>
<template>

    <v-table>

        <thead>
            <tr>

                <th>
                    ID
                </th>
                <th>
                    Nivel

                </th>
                <th>
                    Observações
                </th>
                <th>
                    Data Atualização
                </th>

            </tr>
        </thead>
        <tbody>
            <tr v-for="informativo in informativoLixeira" :key="informativo.id">
                <td>{{ informativo.idInformativoLixeira }}</td>
                <td>{{ informativo.nivelLixeira }}</td>
                <td>{{ informativo.observacao }}</td>
                <td>{{ informativo.dataAtualizacao }}</td>
            </tr>
        </tbody>

    </v-table>

</template>
