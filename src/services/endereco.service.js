import axios from "axios";

const {

    VITE_API_ESTADO,
    VITE_API_CIDADE,
    VITE_API_ENDERECO_POR_CEP

} = import.meta.env


export async function getEstados(useEstadoStore) {

    const retorno = await axios.get(VITE_API_ESTADO)

    if (retorno.status == 200) {

        useEstadoStore().addEstado(retorno.data.map((linha) => linha.estado))
        return true;

    }

    return false

}

export async function getCidades(useCidadeStore) {

    const retorno = await axios.get(VITE_API_CIDADE)

    if (retorno.status == 200) {

        useCidadeStore().addCidade(retorno.data.map((linha) => linha.nome))
        useCidadeStore().cidades.sort()

        return true;

    }

    return false

}

export async function getEnderecoPorCep(cep) {

    return await axios.get(`${VITE_API_ENDERECO_POR_CEP}/${cep}`)

}