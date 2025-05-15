<script setup lang="js">

//Pinia
import { storeToRefs } from 'pinia'

//Gerenciadores de estado
import { useInformativoLixeiraStore } from '@/stores/informativoLixeira'
const informativoLixeiraStore = useInformativoLixeiraStore()
const { informativosLixeira } = storeToRefs(useInformativoLixeiraStore())

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
            <tr v-for="informativo in informativosLixeira" :key="informativo.id_informativo">
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
