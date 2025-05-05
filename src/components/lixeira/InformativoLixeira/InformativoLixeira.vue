<script setup lang="js">

import { watch } from 'vue'

import { informativoLixeira, getInformativoLixeiraPorPontoLixoId } from '../../../services/informativo.lixeira.service.js'

const props = defineProps({
    lixeiraSelecionada: {
        type: Object,
        required: true
    }
})

watch(() => props.lixeiraSelecionada.ponto_lixo_id, () => {


    getInformativoLixeiraPorPontoLixoId(props.lixeiraSelecionada.ponto_lixo_id);

})

getInformativoLixeiraPorPontoLixoId(props.lixeiraSelecionada.ponto_lixo_id);

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
                <td>{{ informativo.id_informativo }}</td>
                <td>{{ informativo.nivel_lixeira }}</td>
                <td>{{ informativo.observacao }}</td>
                <td>{{ informativo.criado_em }}</td>
                <td><v-chip v-if="informativo.informado_por_id">{{ informativo.informado_por_id == 1 ? 'Usuário' :
                    informativo.informado_por_id == 2 ?
                        'Microcontrolador ESP32' : '' }}</v-chip></td>
            </tr>
        </tbody>

    </v-table>

</template>
