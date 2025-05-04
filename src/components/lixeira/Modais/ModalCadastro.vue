<script setup lang="js">

import { getGrupoLixeira, limparCampos, cadastrarGrupoPontoLixoLixeira, form } from '../../../services/lixeira.service'
import FormularioCadastroLixeira from '../Formularios/FormularioCadastroLixeira.vue'
import { ref } from 'vue'

defineProps({
    data: Object
})

async function cadastrarLixeira() {

    const retorno = await cadastrarGrupoPontoLixoLixeira(form.value);

    if (retorno) {

        getGrupoLixeira();

    }


}

</script>

<template>


    <v-dialog v-model="data.exibir" max-width="900">
        <template v-slot:default="{ isActive }">

            <v-card>

                <FormularioCadastroLixeira></FormularioCadastroLixeira>

                <template v-slot:actions>
                    <v-btn variant="flat" color="rgb(94, 93, 93)" @click="limparCampos()">
                        Limpar Campos
                    </v-btn>
                    <v-btn variant="flat" color="rgb(94, 93, 93)" text="CADASTRAR LIXEIRA"
                        @click="cadastrarLixeira()"></v-btn>
                    <v-btn variant="flat" color="rgb(94, 93, 93)" text="Fechar" @click="data.exibir = false"></v-btn>
                </template>

            </v-card>
        </template>
    </v-dialog>

</template>