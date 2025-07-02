import { ref } from 'vue'
import { defineStore } from 'pinia'
import { materiaisReciclaveisComChaveValor } from '../services/materiais.reciclaveis.services.js'

export const useMaterialReciclavelStore = defineStore('material_reciclavel', {

    state: () => ({

        materialReciclavel: {},
        materiaisReciclaveis: ref([])

    }),

    actions: {

        getMaterialReciclavel() {

            this.materiaisReciclaveis = materiaisReciclaveisComChaveValor.value

            console.log(this.materiaisReciclaveis)

        }

    }

})