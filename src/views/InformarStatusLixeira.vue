<script setup lang="js">
import BarraSuperior from '@/components/lixeira/BarraSuperior/BarraSuperior.vue';
import DetalheLixeira from '@/components/lixeira/DetalheLixeira/DetalheLixeira.vue';
import TituloPagina from '@/components/lixeira/Titulo/TituloPagina.vue';
import { mdiInformation } from '@mdi/js';
import { getLixeirasQuery, form, atualizarNivelLixeira,cadastrarInformativoLixeira } from '../components/lixeira/lixeira.service.js'
import { onMounted, ref, watch } from 'vue';
import { niveisLixeira } from '../components/lixeira/nivel.lixeira.service.js'

const configuracaoTitulo = {

    nome: 'Dados Lixeira',
    icone: mdiInformation,

}

const idLixeira = window.location.href.split("/").pop();
const lixeira = ref({});

onMounted(() => {

    getLixeirasQuery({ id: idLixeira }).then((res) => {


        lixeira.value = res[0];


    })
    

})

function atualizarViewEmTempoRealAposSelectDeNovoNivelLixeira() {

    const nivel = niveisLixeira.filter((nivel) => nivel.descricaoComoTexto == form.value.lixeiras[0].nivelLixeira)
    lixeira.value.nivelLixeira = `${nivel[0].valor}`

}

function monitarMudancasNoSelectNoNovoNivelLixeira() {

    return form.value.lixeiras[0].nivelLixeira
}

watch(() => monitarMudancasNoSelectNoNovoNivelLixeira(), () => {

    atualizarViewEmTempoRealAposSelectDeNovoNivelLixeira();

})

function atualizarLixeira() {

    atualizarNivelLixeira(lixeira.value);

    const informativoLixeira = {

        pontoLixoId:lixeira.value.pontoLixoId,
        nivelLixeira:lixeira.value.nivelLixeira,
        observacao:form.value.lixeiras[0].observacao,
        dataAtualizacao: new Date().toISOString().split('T')[0],
        horaAtualizacao: new Date().toLocaleTimeString('pt-BR', { hour12: false }).split(' ')[0],
        informadoPor:"Usuário"
    }

    cadastrarInformativoLixeira(informativoLixeira);


}


</script>

<template>


    <BarraSuperior>

        <template v-slot:titulo>

            <TituloPagina :configuracaoTitulo="configuracaoTitulo"></TituloPagina>

        </template>

    </BarraSuperior>
    <DetalheLixeira :lixeira="lixeira" v-if="lixeira"></DetalheLixeira>

    <BarraSuperior>

        <template v-slot:titulo>

            <TituloPagina :configuracaoTitulo="{ nome: 'Atualizar Informação Lixeira', icone: mdiInformation }">
            </TituloPagina>

        </template>

    </BarraSuperior>

    <v-sheet class="mx-auto" width="100%" height="100%">

        <v-form>
            <v-row>
                <v-col cols="4" sm="12">
                    <v-select label="Nivel Lixeira"
                        :items="niveisLixeira.map((descricoes) => descricoes.descricaoComoTexto)"
                        v-model="form.lixeiras[0].nivelLixeira"></v-select>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="4" sm="12">
                    <v-text-field label="Observação" v-model="form.lixeiras[0].observacao"></v-text-field>
                </v-col>
            </v-row>
            <div class="d-flex justify-end">
                <v-btn variant="flat" color="rgb(94, 93, 93)" text="ATUALIZAR NIVEL LIXEIRA"
                    @click="atualizarLixeira()"></v-btn>
            </div>
        </v-form>

    </v-sheet>


</template>