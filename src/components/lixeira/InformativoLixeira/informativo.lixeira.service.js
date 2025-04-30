
import { ref } from 'vue'


const baseUrl = "http://127.0.0.1:5000";
const apiInformativoLixeira = `${baseUrl}/get_informativo_lixeira`;

export const informativoLixeira = ref([])

export async function getInformativoLixeiraPorPontoLixoId(ponto_lixo_id) {

    fetch(`${apiInformativoLixeira}`, {

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





