const token = localStorage.getItem('token');
const headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${token}`
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