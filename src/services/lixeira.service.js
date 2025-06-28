import { ref } from 'vue'
import { lixeiraModel } from '../components/lixeira/lixeira.model.js'
import axios from 'axios'

const {
    VITE_API_LIXEIRA
}
    = import.meta.env

export const form = ref({
    ...lixeiraModel
})


export async function getLixeira(data) {

    return await axios.post(VITE_API_LIXEIRA, data)

}

