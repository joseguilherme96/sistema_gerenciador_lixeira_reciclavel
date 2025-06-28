import { defineStore } from "pinia";
import axios from "axios";

const contexto = {

    state: () => ({

        filtro: {},
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
        }

    }

}

export const useFiltroGrupoLixeiraStore = defineStore('filtro-grupo-lixeira', contexto)