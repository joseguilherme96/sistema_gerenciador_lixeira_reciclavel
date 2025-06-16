import { post } from "./main.service";

const { VITE_API_GRUPO_LIXEIRA, VITE_API_CADASTRAR_GRUPO_LIXEIRA } = import.meta.env

export async function getGrupoLixeira() {

    const retorno = await post({

        enderecoAPI: VITE_API_GRUPO_LIXEIRA,

    })

    if (retorno) {

        return retorno.body

    }

    return false

}

export async function criarGrupoLixeira(GrupoLixeira) {


    const retorno = await post({

        enderecoAPI: VITE_API_CADASTRAR_GRUPO_LIXEIRA,
        body: GrupoLixeira

    })

    if (retorno) {


        return retorno.body

    }

}
