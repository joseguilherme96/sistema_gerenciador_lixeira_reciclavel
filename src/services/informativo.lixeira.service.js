import axios from "axios";

const {

    VITE_API_INFORMATIVO_LIXEIRA,
    VITE_API_CADASTRAR_INFORMATIVO_LIXEIRA

} = import.meta.env

export async function getInformativoLixeiraPorPontoLixoId(informativoLixeiraStore, ponto_lixo_id) {


    const retorno = await axios.post(VITE_API_INFORMATIVO_LIXEIRA, { ponto_lixo_id })

    if (retorno.status == 200) {

        informativoLixeiraStore().carregarTodosInformativos(retorno.data);
        informativoLixeiraStore().ordernarPorOrdemDecrescente()

        if (retorno.status == 404) {

            informativoLixeiraStore().limparInformativo()

        }

        return true;
    }

    return false

}

export async function cadastrarInformativoLixeira(informativo) {

    return await axios.post(VITE_API_CADASTRAR_INFORMATIVO_LIXEIRA, informativo)

}





