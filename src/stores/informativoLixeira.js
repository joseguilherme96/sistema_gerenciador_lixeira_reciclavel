import { ref } from 'vue'
import { defineStore } from 'pinia'

import { cadastrarInformativoLixeira } from '../services/informativo.lixeira.service.js'

export const useInformativoLixeiraStore = defineStore('informativo_lixeira', {

    state: () => ({

        informativosLixeira: ref([])

    }),

    actions: {

        addInformativo(informativo) {

            this.informativosLixeira = informativo

        },

        limparInformativo() {

            this.informativosLixeira = []

        },

        async cadastrarInformativo(informativoLixeira) {


            const retorno = await cadastrarInformativoLixeira(informativoLixeira)


        }

    }

})