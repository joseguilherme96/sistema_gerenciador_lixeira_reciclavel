import { defineStore } from "pinia";
import axios from "axios";

const contexto = {

    state: () => ({

        filtro: {},
        filtros: [],
        resultadoFiltro: [],
        filtroEstaAberto: false

    }),
    actions: {

        async filtrar(VITE_API_GRUPO_LIXEIRA) {

            await axios.post(VITE_API_GRUPO_LIXEIRA, this.filtro)
                .then((res) => {

                    this.resultadoFiltro = res.data

                })
        },

        limparFiltro() {

            this.filtro = {}
        },

        criarFiltros(filtros) {

            this.filtros = filtros

        },

        abrirFecharFiltro() {

            this.filtroEstaAberto = !this.filtroEstaAberto
        }

    }

}

export const useFiltroGrupoLixeiraStore = defineStore('filtro-grupo-lixeira', contexto)
export const useFiltroRelatorioLixeiraStore = defineStore('filtro-relatorio-lixeira', contexto)