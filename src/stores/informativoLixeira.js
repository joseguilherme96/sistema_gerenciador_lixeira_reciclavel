import { ref } from 'vue'
import { defineStore } from 'pinia'

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

        }

    }

})