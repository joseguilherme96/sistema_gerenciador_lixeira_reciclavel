<script setup lang="js">

import {watch} from 'vue'

import {informativoLixeira,getInformativoLixeiraPorPontoLixoId } from './informativo.lixeira.service.js'

const props = defineProps({
    lixeiraSelecionada:{
        type: Object,
        required: true
    }
})

watch(()=>props.lixeiraSelecionada.pontoLixoId, () => {

    getInformativoLixeiraPorPontoLixoId(props.lixeiraSelecionada.pontoLixoId);

})

getInformativoLixeiraPorPontoLixoId(props.lixeiraSelecionada.pontoLixoId);

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
                <th>
                    Atualizado Por :
                </th>

            </tr>
        </thead>
        <tbody>
            <tr v-for="informativo in informativoLixeira" :key="informativo.id">
                <td>{{ informativo.id }}</td>
                <td>{{ informativo.nivelLixeira }}</td>
                <td>{{ informativo.observacao }}</td>
                <td>{{ informativo.dataAtualizacao }}</td>
                <td><v-chip>{{ informativo.informadoPor }}</v-chip></td>
            </tr>
        </tbody>

    </v-table>

</template>
