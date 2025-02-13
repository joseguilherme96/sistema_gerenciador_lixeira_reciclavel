
import { ref } from 'vue'
import { lixeiraSelecionada } from '../lixeira.service.js'


const baseUrl = "http://localhost:3000";
const apiInformativoLixeira = `${baseUrl}/informativosLixeira`;

export const informativoLixeira = ref([])

export async function getInformativoLixeiraPorIdLixeira() {

    fetch(`${apiInformativoLixeira}`)
        .then(res => res.json())
        .then(res => {

            informativoLixeira.value = res.filter((informativo) => `${informativo.lixeiraId}` == `${lixeiraSelecionada.value.id}`)

            informativoLixeira.value.sort((a, b) => b.idInformativoLixeira - a.idInformativoLixeira)


        })
        .catch(err => err)

}





