import axios from "axios"
const { VITE_API_CADASTRAR_PONTO_LIXO } = import.meta.env

export async function cadastrarPontoDeLixo(PontoLixo) {


    return axios.post(VITE_API_CADASTRAR_PONTO_LIXO, {})


}