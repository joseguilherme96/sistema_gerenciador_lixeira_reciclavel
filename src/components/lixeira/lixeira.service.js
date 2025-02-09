import { ref, watch } from 'vue'
import { getEnderecoPorCep } from '../../services/endereco.service'
import { lixeiraModel } from './lixeira.model.js'


export const baseUrl = "http://localhost:3000";
export const apiLixeirasUrl = `${baseUrl}/lixeiras`;


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

    fetch(apiLixeirasUrl)
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


export async function getLixeiras() {

    fetch(apiLixeirasUrl)
        .then(res => res.json())
        .then(res => {
            
            lixeira.value = res;

        })
        .catch(err => err)

}

export async function criarLixeira() {


    form.value.data = new Date();
    form.value.hora = new Date().getTime();
    form.value.nivelLixeira = form.value.nivelLixeira.split("%")[0];

    return fetch(apiLixeirasUrl, {
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

