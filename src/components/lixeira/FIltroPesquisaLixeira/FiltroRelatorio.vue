<template>

    <div v-if="filtroEstaAberto">
        <v-row>
            <v-col :cols="filtroList.lg" :sm="filtroList.sm" v-for="filtroList in filtros">
                <v-text-field v-if="!filtroList.items" :label="filtroList.label"
                    v-model="filtro[`${filtroList.vModel}`]" variant="solo"
                    :prepend-inner-icon="filtroList.icon"></v-text-field>
                <v-select v-if="filtroList.items" :label="filtroList.label" variant="solo"
                    :prepend-inner-icon="filtroList.icon"
                    :items="filtroList.items.map((item) => item[`${filtroList.descriptionSelect}`] ? item[`${filtroList.descriptionSelect}`] : typeof item == 'string' ? item : 'null')"
                    v-model="filtro[`${filtroList.vModel}`]"></v-select>
            </v-col>
        </v-row>

        <v-row class="d-flex justify-end">
            <v-col cols="4" sm="2">
                <ButtonPadrao @click="useFiltro.limparFiltro();">
                    Limpar Filtros
                </ButtonPadrao>
            </v-col>
            <v-col cols="4" sm="2">
                <ButtonPadrao @click="useFiltro.filtrar(props.apiBuscaDados)">
                    Pesquisar
                </ButtonPadrao>
            </v-col>
        </v-row>
    </div>

</template>
<script setup>
import ButtonPadrao from '@/components/ButtonPadrao.vue';
import { storeToRefs } from 'pinia';


const props = defineProps({

    useFiltroStore: {
        type: Function
    },
    apiBuscaDados: String

})

const useFiltro = props.useFiltroStore()
const { filtros, filtro, filtroEstaAberto } = storeToRefs(props.useFiltroStore())

/*

    filtros.items pode vir como uma lista de objetos ou pode ser uma lista de valores
    Caso venha como lista de objetos, pega o valor da lista baseado no descriptionSelect.
    Caso contrário pega diretamente o valor


*/



</script>