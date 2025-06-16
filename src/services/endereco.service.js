import { get } from "./main.service"

const {

    VITE_API_ESTADO,
    VITE_API_CIDADE,
    VITE_API_ENDERECO_POR_CEP

} = import.meta.env


export async function getEstados(useEstadoStore) {

    const retorno = await get({

        enderecoAPI: VITE_API_ESTADO

    })

    if (retorno) {

        useEstadoStore().addEstado(retorno.body.map((linha) => linha.estado))

    }

    return false

}

export async function getCidades(useCidadeStore) {

    const retorno = await get({

        enderecoAPI: VITE_API_CIDADE

    })

    if (retorno) {

        useCidadeStore().addCidade(retorno.body.map((linha) => linha.nome))
        useCidadeStore().cidades.sort()

    }

    return false

}

export async function getEnderecoPorCep(cep) {

    const retorno = await get({

        enderecoAPI: `${VITE_API_ENDERECO_POR_CEP}/${cep}`

    })

    if (retorno) {

        return retorno.body

    }


}