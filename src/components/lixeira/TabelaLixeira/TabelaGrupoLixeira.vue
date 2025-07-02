<script setup lang="js">

import { storeToRefs } from 'pinia'
import { onMounted, watch } from 'vue'

// Icones
import { mdiUpdate, mdiViewDashboardOutline } from '@mdi/js'

//Componentes
import BarraProgressoNivelLixeira from '../NivelLixeira/BarraProgressoNivelLixeira.vue'

//Gerenciadores de estado
import { useGrupoLixeiraStore } from '@/stores/grupoLixeira.js'
import { useLixeiraStore } from '@/stores/lixeira'
import { useFiltroGrupoLixeiraStore } from '@/stores/filtro.js'
import ButtonPadrao from '@/components/ButtonPadrao.vue'

const useGrupoLixeira = useGrupoLixeiraStore()
const { lista } = storeToRefs(useGrupoLixeira)
const { resultadoFiltro } = storeToRefs(useFiltroGrupoLixeiraStore())

const useLixeira = useLixeiraStore()

const emit = defineEmits(['abrirModalLixeirasDoGrupoLixeiraSelecionado'])

const abrirModalLixeirasDoGrupoLixeiraSelecionado = async (grupoLixeiraId) => {

    await useLixeira.carregarListaLixeira({ grupo_lixeira_id: grupoLixeiraId })

    emit("abrirModalLixeirasDoGrupoLixeiraSelecionado")

}

onMounted(async () => {

    if (lista.value.length == 0) {

        useGrupoLixeira.carregarLista()

    }

})


//Fica monitorando os resultados da filtragem dos grupos de lixeiras
watch(() => resultadoFiltro.value, (novoValor) => {

    useGrupoLixeira.setGrupo(novoValor)

})


</script>
<template>

    <v-row justify="end">
        <v-btn color="rgb(94, 93, 93)" @click="useGrupoLixeira.carregarLista()">
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
                    Média Nivel de Lixo
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
            <tr v-for="item in lista" :key="item.name">
                <td>{{ item.id_grupo_lixeira }}</td>
                <td>{{ item.nome }}</td>
                <td>{{ item.descricao }}</td>
                <td>{{ item.endereco }}</td>
                <td>{{ item.bairro }}</td>
                <td>{{ item.cidade }}</td>
                <td>{{ item.estado }}</td>
                <td>{{ item.cep }}</td>
                <td>{{ item.capacidade_total_lixo }}</td>
                <td>
                    <BarraProgressoNivelLixeira :item="item"></BarraProgressoNivelLixeira>
                </td>
                <td>{{ item.data }}</td>
                <td>{{ item.hora }}</td>
                <td>
                    <ButtonPadrao @click="abrirModalLixeirasDoGrupoLixeiraSelecionado(item.id_grupo_lixeira)">
                        <svg-icon type="mdi" :path="mdiViewDashboardOutline"></svg-icon>
                        Visualizar
                    </ButtonPadrao>
                </td>
            </tr>
        </tbody>
    </v-table>

</template>