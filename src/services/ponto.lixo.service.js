const { VITE_API_CADASTRAR_PONTO_LIXO } = import.meta.env

export async function cadastrarPontoDeLixo(PontoLixo) {

    try {

        const retornoHeader = await fetch(VITE_API_CADASTRAR_PONTO_LIXO, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({})
        })

        const retornoBody = await retornoHeader.json();

        if (!retornoHeader.ok) {

            throw new Error(retornoBody.message)

        }

        return retornoBody;

    } catch (e) {

        alert(e)

        return false;

    }


}