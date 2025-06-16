import { ref } from 'vue'
import { defineStore } from 'pinia'

import { getGrupoLixeira } from '../services/grupo.lixeira.service'


const estadoInicial = {

    id_grupo_lixeira: '',
    nome: '',
    descricao: '',
    cep: '',
    endereco: '',
    bairro: '',
    cidade: '',
    estado: '',
    uf: '',
    data: '',
    hora: ''


}

export const useGrupoLixeiraStore = defineStore('grupo_lixeira', {


    state: () => ({

        grupoLixeira: ref({ ...estadoInicial }),
        lista: ref([])

    }),

    actions: {

        addGrupo(grupoLixeira) {

            this.lista.unshift(grupoLixeira)

        },

        async carregarLista() {

            const grupoLixeira = await getGrupoLixeira()

            if (grupoLixeira) {

                this.lista = grupoLixeira

                this.lista.sort((a, b) => new Date(b.id_grupo_lixeira) - new Date(a.id_grupo_lixeira))

            }

        },


    }

})