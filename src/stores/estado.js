import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useEstadoStore = defineStore('estado', {

    state: () => ({

        estados: ref([])

    }),

    actions: {

        addEstado(estado) {

            this.estados = estado

        }

    }

})