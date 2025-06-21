<script setup lang="js">

// Vue
import { ref, watch } from 'vue'

// Componentes
import BarraSuperior from '../BarraSuperior/BarraSuperior.vue'
import TituloPagina from '../Titulo/TituloPagina.vue'

// Serviços
import { corLixeira } from '../../../services/cor.lixeira.service.js'
import { niveisLixeira } from '../../../services/nivel.lixeira.service.js'
import { materiaisReciclaveisComChaveValor } from '../../../services/materiais.reciclaveis.services.js'
import { getEnderecoPorCep } from '../../../services/endereco.service'

// Gerenciadores de estado
import { useGrupoLixeiraStore } from '@/stores/grupoLixeira'
import { useLixeiraStore } from '@/stores/lixeira'
import { useEstadoStore } from '@/stores/estado'
import { useCidadeStore } from '@/stores/cidade'

// Icones
import { mdiAccount, mdiAccountPlus, mdiDatabase, mdiPlus, mdiTruck } from '@mdi/js'

//Global
import { exibirMensagemErro } from '@/global.js'


//Gerenciadores de estado
const estados = ref(useEstadoStore().estados)
const cidades = ref(useCidadeStore().cidades)
const { grupoLixeira } = useGrupoLixeiraStore()
const { lixeiras } = useLixeiraStore()

const configuracaoTitulo = {

    nome: 'Cadastro Local Lixeira',
    icone: mdiAccountPlus

}

const configuracaoTitulo1 = {
    nome: 'Cadastro de Lixeiras Neste Local',
    icone: mdiAccountPlus
}

const quantidadeLixeira = ref(1)

const ocultarBotaoAdicionarLixeira = (index) => {

    lixeiras[index].exibirBotaoAdicionarLixeira = false

}

const criarEspacoParaArmazenamentoDaLixeira = () => {

    ocultarBotaoAdicionarLixeira(quantidadeLixeira.value - 1);

    quantidadeLixeira.value++
    lixeiras.push({ exibirBotaoAdicionarLixeira: true })


}

watch(() => grupoLixeira.cep, async (cep) => {

    if (cep !== undefined && cep.length == 8) {

        let cepLimpo = cep.replace(/[^0-9]/g, '')

        await getEnderecoPorCep(cepLimpo)
            .then(res => {

                grupoLixeira.endereco = res.data.street
                grupoLixeira.bairro = res.data.neighborhood
                grupoLixeira.cidade = res.data.city
                grupoLixeira.estado = res.data.state

            })
            .catch(exibirMensagemErro)

    }

})

</script>

<template>
    <v-container>
        <BarraSuperior>

            <template v-slot:titulo>
                <TituloPagina :configuracaoTitulo="configuracaoTitulo"></TituloPagina>
            </template>

        </BarraSuperior>

        <v-row>

            <v-col cols="4" sm="12">
                <v-text-field label="Nome do Grupo" v-model="grupoLixeira.nome"></v-text-field>
            </v-col>
            <v-col cols="4" sm="12">
                <v-text-field label="Descrição Grupo" v-model="grupoLixeira.descricao"></v-text-field>
            </v-col>
        </v-row>

        <v-row>

            <v-col cols="4" sm="12">
                <v-text-field label="Cep" v-model="grupoLixeira.cep" :maxlength="9"></v-text-field>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="4" sm="6">
                <v-text-field label="Endereço" v-model="grupoLixeira.endereco"></v-text-field>
            </v-col>
            <v-col cols="4" sm="6">
                <v-text-field label="Bairro" v-model="grupoLixeira.bairro"></v-text-field>
            </v-col>
            <v-col cols="4" sm="4">
                <v-select label="Cidade" :items="cidades" v-model="grupoLixeira.cidade"></v-select>
            </v-col>
            <v-col cols="4" sm="4">
                <v-select label="Estado" :items="estados" v-model="grupoLixeira.estado"></v-select>
            </v-col>
        </v-row>

        <BarraSuperior>

            <template v-slot:titulo>
                <TituloPagina :configuracaoTitulo="configuracaoTitulo1"></TituloPagina>
            </template>

        </BarraSuperior>

        <v-card v-for="(lixeira, index) in lixeiras" class="pl-5 pr-5 mt-10">
            <v-card-subtitle>
                Lixeira {{ index + 1 }}
            </v-card-subtitle>
            <v-row>
                <v-col cols="4" sm="8" class="m-4">
                    <v-text-field label="Descricao" v-model="lixeira.descricao"></v-text-field>
                </v-col>
                <v-col cols="4" sm="4">
                    <v-select label="Material Coletado"
                        :items="materiaisReciclaveisComChaveValor.map((material) => material.nome)"
                        v-model="lixeira.material"></v-select>
                </v-col>
                <v-col cols="4" sm="4">
                    <v-text-field label="Capacidade(L)" type="number" v-model="lixeira.capacidade"></v-text-field>
                </v-col>
                <v-col cols="4" sm="4">
                    <v-select label="Nivel Lixeira" :items="niveisLixeira.map((nivel) => nivel.descricaoComPorcentagem)"
                        v-model="lixeira.nivel_lixeira"></v-select>
                </v-col>
                <v-col cols="12" sm="12">
                    <v-select label="Cor" :items="corLixeira.map((cor) => cor.nome)" v-model="lixeira.cor"></v-select>
                </v-col>
                <v-col cols="4" sm="12">
                    <v-text-field label="Observação" v-model="lixeira.observacao"></v-text-field>
                </v-col>
                <v-container class="d-flex justify-end">
                    <v-btn color="rgb(94, 93, 93)" @click="criarEspacoParaArmazenamentoDaLixeira()"
                        v-if="lixeira.exibirBotaoAdicionarLixeira">
                        <svg-icon type="mdi" :path="mdiPlus"></svg-icon>
                        Adicionar mais lixeiras
                    </v-btn>
                </v-container>

            </v-row>
        </v-card>

    </v-container>

</template>