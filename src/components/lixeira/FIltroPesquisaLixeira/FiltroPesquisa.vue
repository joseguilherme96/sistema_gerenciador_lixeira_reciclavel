<script setup lang="js">

// Vue
import { ref, watch } from 'vue'

// Serviços
import { form, filtrarLixeiras, limparCampos } from '../../../services/lixeira.service'
import { niveisLixeira } from '../../../services/nivel.lixeira.service'

// Gerenciadores de Estado
import { useEstadoStore } from '@/stores/estado'
import { useCidadeStore } from '@/stores/cidade'


const exibirCalendario = ref(false)
const dataSelecionada = ref(null)

const estados = ref(useEstadoStore().estados)
const cidades = ref(useCidadeStore().cidades)


function pesquisar() {

    filtrarLixeiras(form.value)

}


watch(() => dataSelecionada.value, (newValue, oldvalue) => {

    if (newValue !== oldvalue) {

        let novaData = new Date(dataSelecionada.value)
        form.value.data = novaData.toLocaleDateString('pt-BR', { timeZone: 'UTC' })
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
            <v-text-field label="ID Lixeira" v-model="form.grupo_lixeira_id"></v-text-field>
        </v-col>
        <v-col cols="12" sm="4">
            <v-text-field label="Logradouro" v-model="form.endereco"></v-text-field>
        </v-col>
        <v-col cols="12" sm="2">
            <v-select label="Cidade" :items="cidades" v-model="form.cidade"></v-select>
        </v-col>
        <v-col cols="12" sm="2">
            <v-text-field label="Cep" v-model="form.cep"></v-text-field>
        </v-col>
        <v-col cols="12" sm="2">
            <v-text-field label="Bairro" v-model="form.bairro"></v-text-field>
        </v-col>
        <v-col cols="12" sm="2">
            <v-select label="Estado" :items="estados" v-model="form.estado"></v-select>
        </v-col>
        <v-col cols="12" sm="2">
            <v-text-field label="Capacidade(L)" v-model="form.capacidade" type="number"></v-text-field>
        </v-col>
        <v-col cols="12" sm="3">
            <v-select label="Nivel Lixeira(menor/igual)"
                :items="niveisLixeira.map((nivel) => nivel.descricaoComPorcentagem)"
                v-model="form.nivel_lixeira"></v-select>
        </v-col>
        <v-col cols="12" sm="2">
            <v-text-field label="Data" v-model="form.data" @click="exibirCalendario = true"></v-text-field>
        </v-col>
        <v-col cols="12" sm="2">
            <v-text-field label="Hora" v-model="form.hora"></v-text-field>
        </v-col>
    </v-row>
    <v-row class="d-flex justify-end">
        <v-col cols="4" sm="2">
            <v-btn color="primary" @click="limparCampos()">
                Limpar Filtro
            </v-btn>
        </v-col>
        <v-col cols="4" sm="2">
            <v-btn color="primary" @click="pesquisar()">
                Pesquisar
            </v-btn>
        </v-col>
    </v-row>
</template>