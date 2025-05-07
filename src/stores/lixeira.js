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

            const lixeiras = await getLixeira(where)

            if (lixeiras) {

                this.listaLixeira = lixeiras

            }

        },

        async carregarLixeira(where) {

            const lixeiras = await getLixeira(where)

            if (lixeiras) {

                this.lixeira = lixeiras[0]

            }

        },

        setLixeira(lixeira) {

            this.lixeira = lixeira

        },

        async atualizarNivelLixeira(dados) {

            const lixeira = await atualizarNivelLixeira(dados);

            if (lixeira) {

                this.listaLixeira = this.listaLixeira.filter((item) => item.id_lixeira !== lixeira.dados.id_lixeira)
                this.addLixeira(lixeira)

            }

        }

    }

})