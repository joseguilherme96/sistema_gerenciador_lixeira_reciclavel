import axios from "axios"

const { VITE_API_GRUPO_LIXEIRA, VITE_API_CADASTRAR_GRUPO_LIXEIRA } = import.meta.env

export async function getGrupoLixeira() {

    return await axios.post(VITE_API_GRUPO_LIXEIRA, {})

}

export async function criarGrupoLixeira(GrupoLixeira) {

    return await axios.post(VITE_API_GRUPO_LIXEIRA, GrupoLixeira)

}
