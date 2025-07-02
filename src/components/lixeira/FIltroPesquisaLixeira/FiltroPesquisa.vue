<script setup lang="js">

// Vue
import { ref, watch } from 'vue'

// Serviços
import { niveisLixeira } from '../../../services/nivel.lixeira.service'

// Gerenciadores de Estado
import { useEstadoStore } from '@/stores/estado'
import { useCidadeStore } from '@/stores/cidade'
import { useFiltroGrupoLixeiraStore } from '@/stores/filtro.js'
import { storeToRefs } from 'pinia'
import ButtonPadrao from '@/components/ButtonPadrao.vue'


const exibirCalendario = ref(false)
const dataSelecionada = ref(null)

const estados = ref(useEstadoStore().estados)
const cidades = ref(useCidadeStore().cidades)
const useFiltroLixeiraGrupo = useFiltroGrupoLixeiraStore();
const { filtro } = storeToRefs(useFiltroGrupoLixeiraStore())
const { VITE_API_GRUPO_LIXEIRA } = import.meta.env

function pesquisar() {

    useFiltroLixeiraGrupo.filtrar(VITE_API_GRUPO_LIXEIRA)

}

function limparCampos() {

    useFiltroLixeiraGrupo.limparFiltro();


}


watch(() => dataSelecionada.value, (newValue, oldvalue) => {

    if (newValue !== oldvalue) {

        let novaData = new Date(dataSelecionada.value)
        filtro.value.data = novaData.toLocaleDateString('pt-BR', { timeZone: 'UTC' })
    }

})

</script>

<template>

    <v-dialog v-model="exibirCalendario" max-width="340">
        <template v-slot:default="{ isActive }">
            <v-card>
                <v-date-picker color="#310740" v-model="dataSelecionada" label="Data Devolução"
                    class="ml-2"></v-date-picker>
                <div class="d-flex justify-end">
                    <v-btn variant="flat" color="#310740" text="Fechar" @click="exibirCalendario = false"
                        width="100"></v-btn>
                </div>
            </v-card>
        </template>
    </v-dialog>
    <v-row>
        <v-col cols="12" sm="2">
            <v-text-field label="ID Lixeira" v-model="filtro.grupo_lixeira_id"></v-text-field>
        </v-col>
        <v-col cols="12" sm="4">
            <v-text-field label="Logradouro" v-model="filtro.logradouro"></v-text-field>
        </v-col>
        <v-col cols="12" sm="2">
            <v-select label="Cidade" :items="cidades" v-model="filtro.cidade"></v-select>
        </v-col>
        <v-col cols="12" sm="2">
            <v-text-field label="Cep" v-model="filtro.cep"></v-text-field>
        </v-col>
        <v-col cols="12" sm="2">
            <v-text-field label="Bairro" v-model="filtro.bairro"></v-text-field>
        </v-col>
        <v-col cols="12" sm="2">
            <v-select label="Estado" :items="estados" v-model="filtro.estado"></v-select>
        </v-col>
        <v-col cols="12" sm="2">
            <v-text-field label="Capacidade(L)" v-model="filtro.capacidade" type="number"></v-text-field>
        </v-col>
        <v-col cols="12" sm="3">
            <v-select label="Nivel Lixeira(menor/igual)"
                :items="niveisLixeira.map((nivel) => nivel.descricaoComPorcentagem)"
                v-model="filtro.nivel_lixeira_por_grupo_menor_igual_que"></v-select>
        </v-col>
        <v-col cols="12" sm="3">
            <v-select label="Nivel Lixeira(igual)" :items="niveisLixeira.map((nivel) => nivel.descricaoComPorcentagem)"
                v-model="filtro.nivel_lixeira_por_grupo_igual_que"></v-select>
        </v-col>
        <v-col cols="12" sm="3">
            <v-select label="Nivel Lixeira(igual/maior)"
                :items="niveisLixeira.map((nivel) => nivel.descricaoComPorcentagem)"
                v-model="filtro.nivel_lixeira_por_grupo_igual_maior_que"></v-select>
        </v-col>
        <v-col cols="12" sm="2">
            <v-text-field label="Data" v-model="filtro.data" @click="exibirCalendario = true"></v-text-field>
        </v-col>
        <v-col cols="12" sm="2">
            <v-text-field label="Hora" v-model="filtro.hora"></v-text-field>
        </v-col>
    </v-row>
    <v-row class="d-flex justify-end">
        <v-col cols="4" sm="2">
            <ButtonPadrao @click="limparCampos()">
                Limpar Filtro
            </ButtonPadrao>
        </v-col>
        <v-col cols="4" sm="2">
            <ButtonPadrao @click="pesquisar()">
                Pesquisar
            </ButtonPadrao>
        </v-col>
    </v-row>
</template>