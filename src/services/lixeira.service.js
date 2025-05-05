import { ref, watch } from 'vue'
import { getEnderecoPorCep } from './endereco.service.js'
import { lixeiraModel } from '../components/lixeira/lixeira.model.js'
import { corLixeira } from './cor.lixeira.service.js'
import { materiaisReciclaveisComChaveValor } from './materiais.reciclaveis.services.js'

const {
    VITE_API_GRUPO_LIXEIRA,
    VITE_API_CADASTRAR_GRUPO_LIXEIRA,
    VITE_API_CADASTRAR_PONTO_LIXO,
    VITE_API_LIXEIRA,
    VITE_API_CADASTRAR_LIXEIRA,
    VITE_API_CADASTRAR_GRUPO_LIXEIRA_PONTO_LIXO_LIXEIRA,
    VITE_API_ATUALIZAR_LIXEIRA,
    VITE_API_CADASTRAR_INFORMATIVO_LIXEIRA
}
    = import.meta.env

export const grupoSelecionadoLixeira = ref({});
export const lixeira = ref([
    lixeiraModel
])

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


export async function getGrupoLixeira() {

    fetch(VITE_API_GRUPO_LIXEIRA, {

        method: 'POST',
        body: JSON.stringify({ "grupo_lixeira_id": "" }),
        headers: {
            'Content-Type': 'application/json'
        }

    })
        .then(res => res.json())
        .then(res => {

            lixeira.value = res;
            lixeira.value.sort((a, b) => new Date(b.id_grupo_lixeira) - new Date(a.id_grupo_lixeira))

        })
        .catch(err => err)

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

export async function cadastrarGrupoPontoLixoLixeira(form) {

    //Converte nivel_lixeira,nome cor e nome material para
    form.lixeiras.forEach((lixeira, index) => {

        lixeira.nivel_lixeira = lixeira.nivel_lixeira.split("%")[0]
        lixeira.cor_id = corLixeira.filter((cor) => cor.nome == lixeira.cor)[0].cor_id
        lixeira.mat_colet_id = materiaisReciclaveisComChaveValor.value.filter((material) => material.nome == lixeira.material)[0].mat_colet_id

    })

    try {

        const retornoHeader = await fetch(VITE_API_CADASTRAR_GRUPO_LIXEIRA_PONTO_LIXO_LIXEIRA, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(form)
        })

        const retornoBody = await retornoHeader.json();

        if (retornoHeader.status !== 201) {

            throw new Error(retornoBody.message)

        }

        return retornoBody;


    } catch (e) {

        alert(e)
        return false;

    }


}

export async function selecionarGrupoLixeira(grupoLixeiraId) {

    return getLixeira({ 'grupo_lixeira_id': grupoLixeiraId })
        .then(async (res) => {

            grupoSelecionadoLixeira.value = res

        })

}

export async function getLixeira(data) {

    return fetch(`${VITE_API_LIXEIRA}`, {

        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
        }

    })
        .then(res => res.json())
        .then(res =>
            res

        )
        .catch(err => err)

}


export async function atualizarNivelLixeira(lixeira) {

    fetch(`${VITE_API_ATUALIZAR_LIXEIRA}`, {
        method: 'PUT',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(lixeira)
    })
        .then(res => res.json())
        .then(res => res)
        .catch(err => err)

}

export async function cadastrarInformativoLixeira(informativo) {

    return fetch(`${VITE_API_CADASTRAR_INFORMATIVO_LIXEIRA}`, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(informativo)
    })
        .then(res => res.json())
        .then(res => res)
        .catch(err => err)

}

watch(() => form.value.cep, (cep) => {


    if (cep !== undefined && cep.length == 8) {

        let cepLimpo = cep.replace(/[^0-9]/g, '')

        getEnderecoPorCep(cepLimpo).then((res) => {

            form.value.endereco = res.street
            form.value.bairro = res.neighborhood
            form.value.cidade = res.city
            form.value.estado = res.state

        }).catch(err => console.log(err))



    }

})

