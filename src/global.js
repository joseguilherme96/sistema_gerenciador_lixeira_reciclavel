export const userKey = '__gereciador_lixeira_reciclavel_user'

export function exibirMensagemErro(res) {

    if (res && res.response.data.message) {
        alert(res.response.data.message)
    } else if (res) {

        alert(res)
    }

}

export function exibirMensagemSucesso(res) {

    if (res && res.data.message) {
        alert(res.data.message)
    } else if (res) {

        alert(res)
    }

}