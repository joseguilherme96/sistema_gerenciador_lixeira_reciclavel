// Socketio
import io from 'socket.io-client'

//Pinia
import { storeToRefs } from 'pinia';

//Gerenciadores de Estado
import { useLixeiraStore } from '../stores/lixeira';
import { useInformativoLixeiraStore } from '../stores/informativoLixeira';

const { VITE_API_FLASK_BASE_URL } = import.meta.env


const socket = io(`${VITE_API_FLASK_BASE_URL}`);

socket.on('connect', function (e) {
    console.log('Conectado ao servidor');
});

socket.on('atualizacao_lixeira', function (dados) {

    const { lixeira } = storeToRefs(useLixeiraStore())
    if (dados[0].id_lixeira == lixeira.value.id_lixeira) {

        lixeira.value.nivel_lixeira = dados[0].nivel_lixeira
        lixeira.value.esta_aberta = dados[0].esta_aberta

    }

})

socket.on('atualizacao_observacao_lixeira', function (dados) {

    const { addInformativo, informativosLixeira } = useInformativoLixeiraStore()

    const informativos_sao_do_mesmo_ponto_lixo_id = informativosLixeira.every((item) => item.ponto_lixo_id == dados.ponto_lixo_id)

    if (informativos_sao_do_mesmo_ponto_lixo_id) {

        addInformativo(dados);

    }

})

