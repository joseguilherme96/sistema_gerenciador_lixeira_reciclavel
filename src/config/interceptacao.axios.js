// O objetivo deste arquivo é inteceptar respostas 401(Acesso não autorizado) fazendo com que o usuário seja
// redirecionado para página de login

import axios from "axios";

function redirecionarParaPaginaDeLogin() {

    window.location.href = '/'

}

const success = res => res
const error = err => {

    if (err.response.status === 401) {

        redirecionarParaPaginaDeLogin()

    } else {
        return Promise.reject(err)
    }

}

axios.interceptors.response.use(success, error)