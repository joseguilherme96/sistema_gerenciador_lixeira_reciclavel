import { post } from "./main.service";

const {

    VITE_API_INFORMATIVO_LIXEIRA,
    VITE_API_CADASTRAR_INFORMATIVO_LIXEIRA

} = import.meta.env

export async function getInformativoLixeiraPorPontoLixoId(informativoLixeiraStore, ponto_lixo_id) {


    const retorno = await post({

        enderecoAPI: `${VITE_API_INFORMATIVO_LIXEIRA}`,
        body: { ponto_lixo_id },

    })

    if (retorno) {

        informativoLixeiraStore().carregarTodosInformativos(retorno.body);
        informativoLixeiraStore().ordernarPorOrdemDecrescente()

        if (retorno.status == 404) {

            informativoLixeiraStore().limparInformativo()

        }

        return true;
    }

    return false

}

export async function cadastrarInformativoLixeira(informativo) {

    const retorno = await post({

        enderecoAPI: `${VITE_API_CADASTRAR_INFORMATIVO_LIXEIRA}`,
        body: informativo
    })

    if (retorno) {

        return retorno.body

    }

}





