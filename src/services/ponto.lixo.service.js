import { post } from "./main.service"
const { VITE_API_CADASTRAR_PONTO_LIXO } = import.meta.env

export async function cadastrarPontoDeLixo(PontoLixo) {

    const retorno = post({

        enderecoAPI: VITE_API_CADASTRAR_PONTO_LIXO,
    })

    if (retorno) {

        return retorno.body

    }

    return


}