import { put } from "./main.service"
const { VITE_API_ATUALIZAR_LIXEIRA } = import.meta.env

export const niveisLixeira = [
    { descricaoComPorcentagem: '0%', descricaoComoTexto: "A lixeira está vazia", valor: 0 },
    { descricaoComPorcentagem: '25%', descricaoComoTexto: "A lixeira está com nivel baixo", valor: 25 },
    { descricaoComPorcentagem: '50%', descricaoComoTexto: "A lixeira está na metade", valor: 50 },
    { descricaoComPorcentagem: '75%', descricaoComoTexto: "A lixeira quase cheia", valor: 75 },
    { descricaoComPorcentagem: '100%', descricaoComoTexto: "A lixeira está cheia", valor: 100 }
]

export async function atualizarNivelLixeira(lixeira) {

    const retorno = put({
        enderecoAPI: `${VITE_API_ATUALIZAR_LIXEIRA}`,
        method: 'PUT',
        body: lixeira
    })

    if (retorno) {

        return retorno.body
    }

    return false

}