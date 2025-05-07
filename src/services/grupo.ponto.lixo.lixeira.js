const { VITE_API_CADASTRAR_GRUPO_LIXEIRA_PONTO_LIXO_LIXEIRA } = import.meta.env

import { corLixeira } from '../services/cor.lixeira.service'
import { materiaisReciclaveisComChaveValor } from '../services/materiais.reciclaveis.services'

export async function cadastrarGrupoPontoLixoLixeira(form) {

    //Converte nivel_lixeira,nome cor e nome material para
    form.lixeiras.forEach((lixeira, index) => {

        lixeira.nivel_lixeira = lixeira.nivel_lixeira.split("%")[0]
        lixeira.cor_id = corLixeira.filter((cor) => cor.nome == lixeira.cor)[0].cor_id
        lixeira.mat_colet_id = materiaisReciclaveisComChaveValor.value.filter((material) => material.nome == lixeira.material)[0].mat_colet_id

    })

    try {

        const retornoHeader = await fetch(VITE_API_CADASTRAR_GRUPO_LIXEIRA_PONTO_LIXO_LIXEIRA, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(form)
        })

        const retornoBody = await retornoHeader.json();

        if (retornoHeader.status !== 201) {

            throw new Error(retornoBody.message)

        }

        alert(retornoBody.message)
        return retornoBody;


    } catch (e) {

        alert(e)
        return false;

    }


}