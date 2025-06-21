//Será removido está arquivo e substituido requisições com axios..

const headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc1MDUyNjA1MSwianRpIjoiMTIyYTdiMDAtN2EzMi00NWU0LWIwOWEtNDhmNzAwMmM5NDM0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImRlZmF1bHQiLCJuYmYiOjE3NTA1MjYwNTEsImNzcmYiOiI4NDk0M2VlMC02ODA2LTQ2ZjEtYTE4Mi03ZGJjODcyMWZiY2QiLCJleHAiOjE3NTA1MjY5NTF9.AsHtgk1v3Qu4XcVXiZ77J6UXYNYgzKjeTIwkXPP2QWY`
}

export async function validarResposta(retorno) {

    try {

        const retornoBody = await retorno.json()

        //Acesso não autorizado
        if (retorno.status == 401) {
            return false
        }

        if (retorno.status == 201) {

            alert(retornoBody.message)

            return {
                status: retorno.status,
                body: retornoBody
            }

        }

        if (retorno.status == 404) {

            alert(retornoBody.message)
            return []

        }

        if (retorno.status !== 200) {

            throw new Error(retornoBody.message)

        }

        if (retorno.status == 200) {

            return {
                status: retorno.status,
                body: retornoBody
            };
        }

    } catch (e) {
        alert(e)
        return false
    }

}

export async function post(dados) {

    const retorno = await fetch(dados.enderecoAPI, {
        method: 'POST',
        body: JSON.stringify(dados.body || {}),
        headers
    })

    const retornoService = await validarResposta(retorno)

    if (retornoService) {
        return retornoService
    }

    return false

}

export async function get(dados) {

    const retorno = await fetch(dados.enderecoAPI, {
        method: 'GET',
        headers
    })

    const retornoService = await validarResposta(retorno)


    if (retornoService) {
        return retornoService
    }

    return false
}

export async function put(dados) {

    const retorno = await fetch(dados.enderecoAPI, {
        method: 'PUT',
        body: JSON.stringify(dados.body || {}),
        headers
    })

    const retornoService = await validarResposta(retorno)

    if (retornoService) {

        return retornoService

    }

    return false

}