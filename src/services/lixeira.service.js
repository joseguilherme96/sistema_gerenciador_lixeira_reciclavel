import { post } from './main.service.js'
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

    const retorno = post({

        enderecoAPI: VITE_API_GRUPO_LIXEIRA,
        body: JSON.stringify(form),

    })

    if (retorno) {
        lixeira.value = retorno.body
    }

}


export async function cadastrarLixeira(lixeiras) {

    const retorno = await post({
        enderecoAPI: VITE_API_CADASTRAR_LIXEIRA,
        body: JSON.stringify(lixeiras)
    })

    if (retorno) {

        return retorno.body

    }

}

export async function getLixeira(data) {

    const retorno = await post({

        enderecoAPI: `${VITE_API_LIXEIRA}`,
        body: data,

    })

    if (retorno) {

        return retorno.body
    }

    return false

}

