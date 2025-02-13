<script setup lang="js">

import {form} from '../lixeira.service.js'
import {corLixeira} from '../cor.lixeira.service.js'
import { materiaisReciclaveis } from '../materiais.reciclaveis.services.js'
import {niveisLixeira} from '../nivel.lixeira.service.js'
import BarraSuperior from '../BarraSuperior/BarraSuperior.vue'
import {cidades,estados} from '../../../services/endereco.service.js'


</script>

<template>
    <v-container>
                <BarraSuperior></BarraSuperior>
                
                    <v-row>

                        <v-col cols="4" sm="12" >
                            <v-text-field label="Cep" v-model="form.cep" :maxlength="9"></v-text-field>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="4" sm="6">
                            <v-text-field label="Endereço" v-model="form.endereco"></v-text-field>
                        </v-col>
                        <v-col cols="4" sm="6">
                            <v-text-field label="Bairro" v-model="form.bairro"></v-text-field>
                        </v-col>
                        <v-col cols="4" sm="4">
                            <v-select label="Cidade" :items="cidades" v-model="form.cidade"></v-select>
                        </v-col>
                        <v-col cols="4" sm="4">
                            <v-select label="Estado" :items="estados" v-model="form.estado"></v-select>
                        </v-col>
                        <v-col cols="4" sm="4">
                            <v-select label="Material Coletado" :items="materiaisReciclaveis"
                                v-model="form.materialColetado"></v-select>
                        </v-col>
                        <v-col cols="4" sm="4">
                            <v-text-field label="Capacidade(L)" type="number" v-model="form.capacidade"></v-text-field>
                        </v-col>
                        <v-col cols="4" sm="4">
                            <v-select label="Nivel Lixeira" :items="niveisLixeira" v-model="form.nivelLixeira"></v-select>
                        </v-col>
                        <v-col cols="4" sm="4">
                            <v-select label="Cor" :items="corLixeira" v-model="form.cor"></v-select>
                        </v-col>
                        <v-col cols="4" sm="12">
                            <v-text-field label="Observação" v-model="form.observacao"></v-text-field>
                        </v-col>
                    </v-row>
                </v-container>

</template>