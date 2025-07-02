<template>

    <h5 class="text-h5 mb-5 d-flex justify-space-between" style="color: rgb(54, 76, 54);">
        <svg-icon type="mdi" :path="mdiChartGantt" color="rgb(54, 76, 54)" size="40"></svg-icon>
        Relatório de Acompanhamento dos Niveis das Lixeiras
        <ButtonPadrao @click="useFiltroRelatorioLixeira.abrirFecharFiltro()">
            <svg-icon type="mdi" :path="filtroEstaAberto ? mdiEye : mdiEyeOff"></svg-icon>
            Filtro Lixeiras
        </ButtonPadrao>
    </h5>
    <FiltroRelatorio :useFiltroStore="useFiltroRelatorioLixeiraStore" :apiBuscaDados="VITE_API_LIXEIRA_GRUPO_LIXEIRA">
    </FiltroRelatorio>
    <v-data-table :items="dados" :fixed-header="true" :hover="true" show-select :headers="headers"></v-data-table>

</template>
<script setup>

//Módulos
import { ref, watch } from 'vue'
import { storeToRefs } from 'pinia'
import { mdiEye, mdiEyeOff, mdiChartGantt, mdiIdentifier } from '@mdi/js'

// Serviços
import { getLixeiraGrupoLixeira } from '@/services/lixeira.service.js'

// Componentes
import FiltroRelatorio from '@/components/lixeira/FiltroPesquisaLixeira/FiltroRelatorio.vue'

// Gerenciadores de Estado
import { useFiltroRelatorioLixeiraStore } from '@/stores/filtro.js'
import { useCidadeStore } from '@/stores/cidade'
import { useEstadoStore } from '@/stores/estado'
import { useMaterialReciclavelStore } from '@/stores/MaterialReciclavel.js'
import { useTableRelatorioLixeiraGrupoLixeiraStore } from '@/stores/table.js'
import ButtonPadrao from '@/components/ButtonPadrao.vue'


// ENDPOINT
const { VITE_API_LIXEIRA_GRUPO_LIXEIRA } = import.meta.env

const { cidades } = storeToRefs(useCidadeStore())
const { estados } = storeToRefs(useEstadoStore())
const { materiaisReciclaveis } = storeToRefs(useMaterialReciclavelStore())

// Estado Filtro
const useFiltroRelatorioLixeira = useFiltroRelatorioLixeiraStore();
const { resultadoFiltro, filtroEstaAberto } = storeToRefs(useFiltroRelatorioLixeiraStore())

//Estado Table
const useTableRelatorioLixeiraGrupoLixeira = useTableRelatorioLixeiraGrupoLixeiraStore();
const { dados } = storeToRefs(useTableRelatorioLixeiraGrupoLixeiraStore())

useFiltroRelatorioLixeira.criarFiltros([

    {
        label: "ID Grupo Lixeira",
        vModel: "grupo_lixeira_id",
        sm: 2,
        cols: 12,
        icon: 'mdi-identifier'
    },
    {
        label: "ID Lixeira",
        vModel: "lixeira_id",
        sm: 2,
        cols: 12,
        icon: 'mdi-identifier'
    },
    {
        label: "Material Coletado",
        vModel: "material_coletado",
        items: materiaisReciclaveis,
        descriptionSelect: 'nome',
        sm: 4,
        cols: 12,
        icon: "mdi-recycle"
    },
    {
        label: "Nivel Lixeira(Menor/Igual que)",
        vModel: "nivel_lixeira_menor_igual_que",
        sm: 4,
        cols: 12,
        icon: 'mdi-hydraulic-oil-level'
    },
    {
        label: "Nivel Lixeira(Igual que)",
        vModel: "nivel_lixeira_igual_que",
        sm: 4,
        cols: 12,
        icon: 'mdi-hydraulic-oil-level'
    },
    {
        label: "Nivel Lixeira(Maior que)",
        vModel: "nivel_lixeira_maior_que",
        sm: 4,
        cols: 12,
        icon: 'mdi-hydraulic-oil-level'
    },
    {
        label: "Cidade",
        vModel: "cidade",
        items: cidades,
        sm: 4,
        cols: 12,
        icon: 'mdi-home-city-outline'
    },
    {
        label: "Estado",
        vModel: "estado",
        items: estados,
        sm: 4,
        cols: 12,
        icon: 'mdi-diving-scuba-flag '
    }

])

const headers = ref([

    {
        title: "ID Grupo Lixeira",
        value: "grupo_lixeira_id",
        sortable: true,
        checked: true
    },
    {
        title: "ID Lixeira",
        value: "id_lixeira",
        sortable: true,
        checked: true
    },
    {
        title: "Capacidade",
        value: "capacidade",
        sortable: true,
        checked: true
    },
    {
        title: "Material Coletado",
        value: "material_coletado",
        sortable: true,
        checked: true
    },
    {
        title: "Nivel Lixeira",
        value: "nivel_lixeira",
        sortable: true,
        checked: true
    },
    {
        title: "Endereço",
        value: "endereco",
        sortable: true,
        checked: true
    },
    {
        title: "Bairro",
        value: "bairro",
        sortable: true,
        checked: true
    },
    {
        title: "Cidade",
        value: "cidade",
        sortable: true,
        checked: true
    },
    {
        title: "Estado",
        value: "estado",
        sortable: true,
        checked: true
    },


])

useTableRelatorioLixeiraGrupoLixeira.carregarDados(getLixeiraGrupoLixeira({}))

//Fica monitorando os resultados da filtragem das lixeiras
watch(() => resultadoFiltro.value, (novoValor) => {

    useTableRelatorioLixeiraGrupoLixeira.setData(novoValor)

})

</script>