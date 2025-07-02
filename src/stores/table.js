import { defineStore } from "pinia";


const contexto = {

    state: () => ({

        dados: []

    }),
    actions: {

        setData(dados) {

            this.dados = dados

        },
        async carregarDados(callback) {

            callback.then((res) => {

                this.dados = res.data

            })

        }

    }

}

export const useTableRelatorioLixeiraGrupoLixeiraStore = defineStore('relatorio-lixeira-grupo-lixeira', contexto)