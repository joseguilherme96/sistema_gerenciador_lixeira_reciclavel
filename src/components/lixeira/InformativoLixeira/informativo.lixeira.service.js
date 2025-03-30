
import { ref } from 'vue'
import { lixeiraSelecionada } from '../lixeira.service.js'


const baseUrl = "http://localhost:3000";
const apiInformativoLixeira = `${baseUrl}/informativosLixeira`;

export const informativoLixeira = ref([])

export async function getInformativoLixeiraPorPontoLixoId(ponto_lixo_id) {

    fetch(`${apiInformativoLixeira}?pontoLixoId=${ponto_lixo_id}`)
        .then(res => res.json())
        .then(res => {
            
            informativoLixeira.value = res;
            informativoLixeira.value.sort((a, b) => b.idInformativoLixeira - a.idInformativoLixeira)


        })
        .catch(err => err)

}





