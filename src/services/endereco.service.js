import { ref } from 'vue'

const {

    VITE_API_ESTADO,
    VITE_API_CIDADE,
    VITE_API_ENDERECO_POR_CEP

} = import.meta.env


export const estados = ref([
])

export const cidades = ref([
])



export function getEstados() {

    fetch(VITE_API_ESTADO)
        .then(res => res.json())
        .then(res => {

            estados.value = res.map((linha) => linha.estado)
        })
        .catch(err => err)

}

export function getCidades() {

    fetch(VITE_API_CIDADE)
        .then(res => res.json())
        .then(res => {

            cidades.value = res.map((linha) => linha.nome)

            cidades.value.sort()
        })
        .catch(err => err)

}

export async function getEnderecoPorCep(cep) {


    return fetch(`${VITE_API_ENDERECO_POR_CEP}/${cep}`)
        .then(res => res.json())
        .then(res => res)
        .catch(err => err)


}