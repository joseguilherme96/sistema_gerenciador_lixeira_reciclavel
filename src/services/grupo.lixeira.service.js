const { VITE_API_GRUPO_LIXEIRA, VITE_API_CADASTRAR_GRUPO_LIXEIRA } = import.meta.env

export async function getGrupoLixeira() {


    try {

        const retornoHeader = await fetch(VITE_API_GRUPO_LIXEIRA, {

            method: 'POST',
            body: JSON.stringify({ "grupo_lixeira_id": "" }),
            headers: {
                'Content-Type': 'application/json'
            }

        })

        const retornoBody = await retornoHeader.json();

        if (retornoHeader.status !== 200 && retornoHeader.status !== 404) {

            throw new Error(retornoBody.message)

        }

        if (retornoHeader.status !== 404) {

            return retornoBody;
        }

        return []


    } catch (e) {

        alert(e)
        return false

    }

}

export async function criarGrupoLixeira(GrupoLixeira) {

    try {

        let retornoHeader = await fetch(VITE_API_CADASTRAR_GRUPO_LIXEIRA, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(form.value)
        })

        const retornoBody = await retornoHeader.json()

        if (!retornoHeader.ok) {

            throw new Error(retornoBody.message)

        }

        return retornoBody;

    } catch (e) {

        alert(e)
        return false;

    }

}
