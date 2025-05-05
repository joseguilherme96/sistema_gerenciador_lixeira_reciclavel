const {

    VITE_API_INFORMATIVO_LIXEIRA

} = import.meta.env

export async function getInformativoLixeiraPorPontoLixoId(informativoLixeiraStore, ponto_lixo_id) {


    try {

        const retornoHeader = await fetch(`${VITE_API_INFORMATIVO_LIXEIRA}`, {

            method: 'POST',
            body: JSON.stringify({ ponto_lixo_id }),
            headers: {
                'Content-Type': 'application/json'
            }

        })

        const retornoBody = await retornoHeader.json()

        if (retornoHeader.status !== 200 && retornoHeader.status !== 404) {

            throw new Error(retornoBody.message)

        }

        if (retornoHeader.status == 200) {

            informativoLixeiraStore().addInformativo(retornoBody);
            informativoLixeiraStore().informativosLixeira.sort((a, b) => b.id_informativo - a.id_informativo)

        }

        if (retornoHeader.status == 404) {

            informativoLixeiraStore().limparInformativo()

        }

        return true;

    } catch (err) {

        alert(err)
        return false;

    }

}





