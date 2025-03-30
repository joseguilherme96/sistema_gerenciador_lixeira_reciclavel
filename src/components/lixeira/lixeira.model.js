import { lixeira } from "./lixeira.service";

export const lixeiraModel = {

    cep: '',
    endereco: '',
    cidade: '',
    estado: '',
    data: '',
    hora: '',
    lixeiras: [{
        materialColetado: '',
        capacidade: 0,
        nivelLixeira: 0,
        data: '',
        hora: '',
        cor: '',
        exibirBotaoAdicionarLixeira: true
    }]



}