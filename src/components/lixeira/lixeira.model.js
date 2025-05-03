import { lixeira } from "./lixeira.service";

export const lixeiraModel = {

    cep: '',
    endereco: '',
    cidade: '',
    estado: '',
    descricao: '',
    lixeiras: [{
        material: '',
        descricao: '',
        capacidade: 0,
        nivelLixeira: 0,
        cor: '',
        exibirBotaoAdicionarLixeira: true,
        observacao: '',
    }]



}