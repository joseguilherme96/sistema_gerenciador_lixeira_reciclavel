import { ref } from 'vue'
import { defineStore } from 'pinia'

import { cadastrarInformativoLixeira } from '../services/informativo.lixeira.service.js'

export const useInformativoLixeiraStore = defineStore('informativo_lixeira', {

    state: () => ({

        informativosLixeira: ref([])

    }),

    actions: {

        addInformativo(informativo) {

            this.informativosLixeira.unshift(informativo)

        },

        ordernarPorOrdemDecrescente() {

            this.informativosLixeira.sort((a, b) => b.id_informativo - a.id_informativo)

        },

        carregarTodosInformativos(informativos) {

            this.informativosLixeira = informativos

        },

        limparInformativo() {

            this.informativosLixeira = []

        },

        async cadastrarInformativo(informativoLixeira) {


            const retorno = await cadastrarInformativoLixeira(informativoLixeira)

        }

    }

})