<script setup lang="js">

import { ref, watch } from 'vue'
import { form, filtrarLixeiras,limparCampos } from './lixeira.service'
import {niveisLixeira} from './nivel.lixeira.service'
import { estados,cidades } from '../../services/endereco.service'
import {materiaisReciclaveis} from './materiais.reciclaveis.services'

const exibirCalendario = ref(false)
const dataSelecionada = ref(null)



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
            <v-text-field label="ID Lixeira" v-model="form.idLixeira"></v-text-field>
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
        <v-col cols="12" sm="5">
            <v-select label="Materias Coletado"
                :items="materiaisReciclaveis" v-model="form.materialColetado"></v-select>
        </v-col>
        <v-col cols="12" sm="2">
            <v-text-field label="Capacidade(L)" v-model="form.capacidade" type="number"></v-text-field>
        </v-col>
        <v-col cols="12" sm="3">
            <v-select label="Nivel Lixeira(menor/igual)" :items="niveisLixeira"
                v-model="form.nivelLixeira"></v-select>
        </v-col>
    </v-row>
    <v-row>
        <v-col cols="12" sm="2">
            <v-text-field label="Data" v-model="form.data" @click="exibirCalendario = true"></v-text-field>
        </v-col>
        <v-col cols="12" sm="2">
            <v-text-field label="Hora" v-model="form.hora"></v-text-field>
        </v-col>
        <v-col cols="6" sm="2">
            <v-btn color="primary" @click="limparCampos()">
                Limpar Filtro
            </v-btn>
        </v-col>
        <v-col cols="6" sm="2">
            <v-btn color="primary" @click="pesquisar()">
                Pesquisar
            </v-btn>
        </v-col>
    </v-row>
</template>