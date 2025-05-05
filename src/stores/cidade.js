import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useCidadeStore = defineStore('cidade', {

    state: () => ({

        cidades: ref([])

    }),

    actions: {

        addCidade(cidade) {

            this.cidades = cidade

        }

    }

})