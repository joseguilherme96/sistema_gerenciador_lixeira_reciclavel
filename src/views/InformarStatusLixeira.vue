<script setup lang="js">

import { onMounted, ref, watch } from 'vue';
import { storeToRefs } from 'pinia';

//Componentes
import BarraSuperior from '@/components/lixeira/BarraSuperior/BarraSuperior.vue';
import DetalheLixeira from '@/components/lixeira/DetalheLixeira/DetalheLixeira.vue';
import TituloPagina from '@/components/lixeira/Titulo/TituloPagina.vue';

//Icones
import { mdiInformation } from '@mdi/js';

//Services
import { form } from '../services/lixeira.service.js'
import { niveisLixeira } from '../services/nivel.lixeira.service.js'

//Gerenciadores de estado
import { useLixeiraStore } from '@/stores/lixeira'
import { useInformativoLixeiraStore } from '@/stores/informativoLixeira'

const useLixeira = useLixeiraStore()
const { cadastrarInformativo } = useInformativoLixeiraStore()

const { carregarLixeira, atualizarNivelLixeira } = useLixeira
const { lixeira } = storeToRefs(useLixeira)

const configuracaoTitulo = {

    nome: 'Dados Lixeira',
    icone: mdiInformation,

}

const idLixeira = parseInt(window.location.href.split("/").pop());

onMounted(async () => {

    if (lixeira.value.id_lixeira === "" || lixeira.value.id_lixeira !== idLixeira) {

        await carregarLixeira({ lixeira_id: idLixeira })

    }

})

function atualizarViewEmTempoRealAposSelectDeNovoNivelLixeira() {

    const nivel = niveisLixeira.filter((nivel) => nivel.descricaoComoTexto == form.value.lixeiras[0].nivelLixeira)
    lixeira.value.nivel_lixeira = `${nivel[0].valor}`

}

function monitarMudancasNoSelectNoNovoNivelLixeira() {

    return form.value.lixeiras[0].nivelLixeira
}

watch(() => monitarMudancasNoSelectNoNovoNivelLixeira(), () => {

    atualizarViewEmTempoRealAposSelectDeNovoNivelLixeira();

})

async function atualizarLixeira() {

    const retorno = await atualizarNivelLixeira({
        nivel_lixeira: lixeira.value.nivel_lixeira,
        lixeira_id: lixeira.value.id_lixeira,
        esta_aberta: lixeira.value.esta_aberta === "Aberta" ? true : false
    });

    const informativoLixeira = {

        ponto_lixo_id: lixeira.value.ponto_lixo_id,
        informado_por_id: "1",
        nivel_lixeira: lixeira.value.nivel_lixeira,
        observacao: form.value.lixeiras[0].observacao,
    }

    cadastrarInformativo(informativoLixeira);




}


</script>

<template>


    <BarraSuperior style="background-color: var(--btn-bg-primary-color)">

        <template v-slot:titulo>

            <TituloPagina :configuracaoTitulo="configuracaoTitulo"></TituloPagina>

        </template>

    </BarraSuperior>
    <DetalheLixeira :lixeira="lixeira" v-if="lixeira.id_lixeira !== ''"></DetalheLixeira>

    <BarraSuperior class="mt-5" style="background-color: var(--btn-bg-primary-color)">

        <template v-slot:titulo>

            <TituloPagina :configuracaoTitulo="{ nome: 'Atualizar Informação Lixeira', icone: mdiInformation }">
            </TituloPagina>

        </template>

    </BarraSuperior>

    <v-sheet class="mx-auto" width="100%" height="100%">

        <v-form>
            <v-row>
                <v-col cols="12" sm="12">
                    <v-select label="Nivel Lixeira"
                        :items="niveisLixeira.map((descricoes) => descricoes.descricaoComoTexto)"
                        v-model="form.lixeiras[0].nivelLixeira"></v-select>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="12" sm="12">
                    <v-select label="Estado Lixeira" :items='["Aberta", "Fechada"]'
                        v-model="lixeira.esta_aberta"></v-select>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="12" sm="12">
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