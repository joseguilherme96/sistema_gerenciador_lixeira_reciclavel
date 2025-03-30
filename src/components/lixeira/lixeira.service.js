import { ref, watch } from 'vue'
import { getEnderecoPorCep } from '../../services/endereco.service'
import { lixeiraModel } from './lixeira.model.js'


export const baseUrl = "http://localhost:3000";

export const apiEnderecosLixeirasUrl = `${baseUrl}/enderecos_lixeiras`;
export const apiPontosDeLixoComOuSemLixeira = `${baseUrl}/pontos_lixo`
export const apiLixeiras = `${baseUrl}/lixeiras`;


export const lixeiraSelecionada = ref({});
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

    fetch(apiEnderecosLixeirasUrl)
        .then(res => res.json())
        .then(res => {


            let filtro = res.filter((res) => {


                return (res.id == `${form.idLixeira}` && form.idLixeira !== '')
                    || (res.endereco.toLowerCase().includes(`${form.endereco.toLowerCase()}`) && form.endereco !== '')
                    || (res.cidade == form.cidade && form.cidade !== '')
                    || (res.estado == form.estado && form.estado !== '')
                    || (res.materialColetado == form.materialColetado && form.materialColetado !== '')
                    || (res.capacidade == form.capacidade && form.capacidade !== '')
                    || (res.data == form.data && form.data !== '')
                    || (`${new Date(res.data).toLocaleDateString()}` == `${form.data}` && form.data !== '')


            })
            lixeira.value = filtro


        })
        .catch(err => err)
}


export async function getEnderecosLixeiras() {

    fetch(apiEnderecosLixeirasUrl)
        .then(res => res.json())
        .then(res => {

            lixeira.value = res;
            lixeira.value.sort((a, b) => new Date(b.data) - new Date(a.data))

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
        lixeira.endereco_lixeira_id = endereco_lixeira_id

        return lixeira

    })

    form.value.lixeiras.forEach(async (lixeira, index) => {

        let ponto_lixo = await cadastrarPontosDeLixo(true)

        form.value.lixeiras[index].ponto_lixo_id = ponto_lixo.id

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

export async function selecionarLixeira(idLixeira) {

    return getEnderecoLixeiraPorId(idLixeira)
        .then(async (res) => {

            lixeiraSelecionada.value = res

            //Filtra Lixeiras por endereco_lixeira_id
            await getLixeirasQuery({ endereco_lixeira_id: idLixeira }).then((res) => {

                lixeiraSelecionada.value.lixeiras = res
            })

        })

}

export async function getEnderecoLixeiraPorId(idLixeira) {

    return fetch(`${apiEnderecosLixeirasUrl}/${idLixeira}`)
        .then(res => res.json())
        .then(res =>
            res

        )
        .catch(err => err)

}

export async function getLixeirasQuery(where) {

    let query = ``

    if ('endereco_lixeira_id' in where) {

        query = `endereco_lixeira_id=${where.endereco_lixeira_id}`

    }

    if ('ponto_lixo_id' in where) {
        query = `&&ponto_lixo_id=${where.ponto_lixo_id}`

    }

    return fetch(`${apiLixeiras}?${query}`)
        .then(res => res.json())
        .then(res => {

            return res

        }

        )
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

