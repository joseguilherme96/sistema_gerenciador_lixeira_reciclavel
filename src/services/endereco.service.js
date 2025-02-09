import { ref } from 'vue'


export const baseUrl = "http://localhost:3000";
export const apiCidadesUrl = "https://servicodados.ibge.gov.br/api/v1/localidades/distritos"
export const apiCepUrl = "https://brasilapi.com.br/api/cep/v1"


export const estados = ref([
])

export const cidades = ref([
])



export function getEstados() {

    fetch(baseUrl + "/estados")
        .then(res => res.json())
        .then(res => {

            estados.value = res.map((linha) => linha.estado)
        })
        .catch(err => err)

}

export function getCidades() {

    fetch(apiCidadesUrl)
        .then(res => res.json())
        .then(res => {

            cidades.value = res.map((linha) => linha.nome)

            cidades.value.sort()
        })
        .catch(err => err)

}

export async function getEnderecoPorCep(cep) {

 
        return fetch(`${apiCepUrl}/${cep}`)
            .then(res => res.json())
            .then(res => res)
            .catch(err => err)

    
}