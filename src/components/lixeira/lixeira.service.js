import { ref, watch } from 'vue'
import { getEnderecoPorCep } from '../../services/endereco.service'
import { lixeiraModel } from './lixeira.model.js'


export const baseUrl = "http://127.0.0.1:5000";

export const apiEnderecosLixeirasUrl = `${baseUrl}/grupo_lixeira`;
export const apiPontosDeLixoComOuSemLixeira = `${baseUrl}/pontos_lixo`
export const apiLixeiras = `${baseUrl}/get_lixeira`;
export const apiAtualizarLixeira = `${baseUrl}/atualizar_nivel_lixeira`;
export const informativoLixeira = `${baseUrl}/cadastrar_informativo_lixeira`


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

    fetch(apiEnderecosLixeirasUrl, {

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


export async function getEnderecosLixeiras() {

    fetch(apiEnderecosLixeirasUrl, {

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

export async function criarEnderecoLixeira() {


    form.value.data = new Date();
    form.value.hora = new Date().getTime();

    let retorno = await fetch(apiEnderecosLixeirasUrl, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(form.value)
    })
        .then(res => res.json())
        .then(res => res)
        .catch(err => err)

    vincularLixeiraAoEnderecoCadastrado(retorno.id);

}


export async function vincularLixeiraAoEnderecoCadastrado(endereco_lixeira_id) {


    form.value.lixeiras = form.value.lixeiras.map((lixeira) => {

        lixeira.data = new Date();
        lixeira.hora = new Date().getTime();
        lixeira.nivelLixeira = lixeira.nivelLixeira.split("%")[0];
        lixeira.enderecoLixeiraId = endereco_lixeira_id

        return lixeira

    })

    form.value.lixeiras.forEach(async (lixeira, index) => {

        let ponto_lixo = await cadastrarPontosDeLixo(true)
        form.value.lixeiras[index].pontoLixoId = ponto_lixo.id

        await fetch(apiLixeiras, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(lixeira)
        })
            .then(res => res.json())
            .then(res => res)
            .catch(err => err)

    });

}

export async function cadastrarPontosDeLixo(localTemLixeira) {

    let dados = {

        localTemLixeira: localTemLixeira,
        data: new Date(),
        hora: new Date().getTime(),

    }

    return fetch(apiPontosDeLixoComOuSemLixeira, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dados)
    })
        .then(res => res.json())
        .then(res => res)
        .catch(err => err)


}

export async function selecionarGrupoLixeira(grupoLixeiraId) {

    return getLixeira({ 'grupo_lixeira_id': grupoLixeiraId })
        .then(async (res) => {

            grupoSelecionadoLixeira.value = res

        })

}

export async function getLixeira(data) {

    return fetch(`${apiLixeiras}`, {

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

    fetch(`${apiAtualizarLixeira}`, {
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

    return fetch(`${informativoLixeira}`, {
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

