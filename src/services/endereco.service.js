const {

    VITE_API_ESTADO,
    VITE_API_CIDADE,
    VITE_API_ENDERECO_POR_CEP

} = import.meta.env


export function getEstados(useEstadoStore) {

    fetch(VITE_API_ESTADO)
        .then(res => res.json())
        .then(res => {

            useEstadoStore().addEstado(res.map((linha) => linha.estado))

        })
        .catch(err => err)

}

export function getCidades(useCidadeStore) {

    fetch(VITE_API_CIDADE)
        .then(res => res.json())
        .then(res => {

            useCidadeStore().addCidade(res.map((linha) => linha.nome))
            useCidadeStore().cidades.sort()
        })
        .catch(err => err)

}

export async function getEnderecoPorCep(cep) {


    try {

        const retorno = await fetch(`${VITE_API_ENDERECO_POR_CEP}/${cep}`)

        const retornoBody = await retorno.json()

        if (retorno.status !== 200 && retorno.status !== 404) {


            throw new Error(retorno.messsage)

        }

        return retornoBody;

    } catch (e) {

        return false;

    }


}