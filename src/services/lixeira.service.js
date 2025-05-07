import { ref } from 'vue'
import { lixeiraModel } from '../components/lixeira/lixeira.model.js'

const {
    VITE_API_GRUPO_LIXEIRA,
    VITE_API_LIXEIRA,
    VITE_API_CADASTRAR_LIXEIRA
}
    = import.meta.env

export const form = ref({
    ...lixeiraModel
})

export function limparCampos() {

    form.value = { ...lixeiraModel }

}

export function formatarDataParaAmericano(data) {
    const [dia, mes, ano] = data.split("/");
    return `${ano}-${mes}-${dia}`;
}

export function filtrarLixeiras(form) {

    fetch(VITE_API_GRUPO_LIXEIRA, {

        method: 'POST',
        body: JSON.stringify(form),
        headers: {
            'Content-Type': 'application/json'
        },

    })
        .then(res => res.json())
        .then(res => {

            lixeira.value = res


        })
        .catch(err => err)
}


export async function cadastrarLixeira(lixeiras) {

    try {

        const retornoHeader = await fetch(VITE_API_CADASTRAR_LIXEIRA, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(lixeiras)
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

export async function getLixeira(data) {

    try {

        const retorno = await fetch(`${VITE_API_LIXEIRA}`, {

            method: 'POST',
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json'
            }

        })

        const retornoBody = await retorno.json()

        if (retorno.status !== 200 && retorno.status !== 404) {

            throw new Error(retornoBody.message)

        }

        if (retorno.status == 200) {

            return retornoBody

        }

        if (retorno.status == 404) {

            alert(retornoBody.message)
            return false

        }

    } catch (e) {

        alert(e)
        return false;

    }



}

