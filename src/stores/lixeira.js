import { ref } from 'vue'
import { defineStore } from 'pinia'

import { getLixeira } from '../services/lixeira.service'
import { atualizarNivelLixeira } from '../services/nivel.lixeira.service'

const estadoInicial = {

    id_lixeira: '',
    descricao: '',
    mat_colet_id: '',
    grupo_lixeira_id: '',
    ponto_lixo_id: '',
    cor_id: '',
    capacidade: '',
    nivel_lixeira: '',
    observacao: '',
    criado_em: '',
    editado_em: ''


}

export const useLixeiraStore = defineStore('lixeira', {


    state: () => ({

        lixeira: ref({ ...estadoInicial }),
        lixeiras: ref([{ exibirBotaoAdicionarLixeira: true }]), // Usada para cadastro de lixeiras
        listaLixeira: ref([]) // Exibe lixeiras

    }),

    actions: {

        addLixeira(lixeira) {

            this.listaLixeira.unshift(lixeira)

        },

        async carregarListaLixeira(where) {

            await getLixeira(where).then(res => {

                this.listaLixeira = res.data

            })

        },

        async carregarLixeira(where) {

            await getLixeira(where).then(res => {

                this.listaLixeira = res.data[0]

            })

        },

        setLixeira(lixeira) {

            console.log(lixeira)
            this.lixeira = lixeira

        },

        async atualizarNivelLixeira(dados) {

            await atualizarNivelLixeira(dados).then(resp => {

                this.listaLixeira = this.listaLixeira.filter((item) => item.id_lixeira !== resp.data.dados.id_lixeira)
                this.addLixeira(resp.data.dados)

            })
        }

    }

})