
import { ref } from 'vue'

const {

    VITE_API_INFORMATIVO_LIXEIRA

} = import.meta.env

export const informativoLixeira = ref([])

export async function getInformativoLixeiraPorPontoLixoId(ponto_lixo_id) {

    fetch(`${VITE_API_INFORMATIVO_LIXEIRA}`, {

        method: 'POST',
        body: JSON.stringify({ ponto_lixo_id }),
        headers: {
            'Content-Type': 'application/json'
        }

    })
        .then(res => res.json())
        .then(res => {

            informativoLixeira.value = res;
            informativoLixeira.value.sort((a, b) => b.id_informativo - a.id_informativo)


        })
        .catch(err => err)

}





