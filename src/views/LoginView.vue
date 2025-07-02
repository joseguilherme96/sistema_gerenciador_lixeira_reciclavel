<script setup>

import { ref } from 'vue'
import axios from 'axios';

//Navegação programatica
import { useRouter } from 'vue-router'

//Gerenciadores de estado
import { useUserStore } from "@/stores/user.js"

// Global
import { userKey, exibirMensagemErro } from '@/global.js'
import ButtonPadrao from '@/components/ButtonPadrao.vue';


const router = useRouter()
const useUser = useUserStore()
const { VITE_API_LOGIN } = import.meta.env

const user = ref({

    usuario: '',
    senha: '',

})

const entrar = async () => {

    axios.post(VITE_API_LOGIN, user.value)
        .then(res => {

            localStorage.setItem(userKey, JSON.stringify(res.data))
            useUser.setUser(res.data)
            router.push({ path: '/about' })

        })
        .catch(exibirMensagemErro)
}
</script>

<template>

    <v-container class="d-flex flex-column align-center justify-center mt-10" style="width:80vh;height: 80vh;">
        <v-form class="text-center">
            <v-row class="justify-center">
                <v-col cols="auto">
                    <v-img :width="400" :height="400" class="align-center" src="planeta.png"></v-img>
                </v-col>
            </v-row>
            <v-text-field label="Usuario" style="width: 400px" v-model="user.usuario" variant="underlined">
            </v-text-field>
            <v-text-field label="Senha" style="width: 400px" type="password" v-model="user.senha" variant="underlined">
            </v-text-field>
            <v-row class="justify-center mt-5">
                <ButtonPadrao @click="entrar">Entrar</ButtonPadrao>
            </v-row>
        </v-form>
    </v-container>
    <v-row class="d-flex flex-column align-center mb-5 mt-5" style="color: rgb(94, 93, 93);">
        <v-col lg="7" cols="12" sm="12">
            Sistema Gerenciador de Lixeiras Recicláveis Integrado com Microcontrolador ESP32
        </v-col>
    </v-row>

</template>