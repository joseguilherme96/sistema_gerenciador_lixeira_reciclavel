<script setup lang="js">

//Componentes
import FormularioCadastroLixeira from '../Formularios/FormularioCadastroLixeira.vue'

//Serviços
import { limparCampos } from '../../../services/lixeira.service'
import { cadastrarGrupoPontoLixoLixeira } from '../../../services/grupo.ponto.lixo.lixeira.js'

// Gerenciadores de estado
import { useGrupoLixeiraStore } from '@/stores/grupoLixeira.js'
import { useLixeiraStore } from '@/stores/lixeira.js'

const useGrupoLixeira = useGrupoLixeiraStore()
const useLixeira = useLixeiraStore()

defineProps({
    data: Object
})

async function cadastrarGrupoLixeiraLixeira() {

    const formGrupoLixeiraLixeiras = { lixeiras: useLixeira.lixeiras, ...useGrupoLixeira.grupoLixeira }

    const retorno = await cadastrarGrupoPontoLixoLixeira(formGrupoLixeiraLixeiras);

    if (retorno) {

        useGrupoLixeira.addGrupo(retorno.dados_grupo_criado)

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
                        @click="cadastrarGrupoLixeiraLixeira()"></v-btn>
                    <v-btn variant="flat" color="rgb(94, 93, 93)" text="Fechar" @click="data.exibir = false"></v-btn>
                </template>

            </v-card>
        </template>
    </v-dialog>

</template>