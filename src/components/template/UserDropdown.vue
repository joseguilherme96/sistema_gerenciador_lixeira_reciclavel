<template>
    <div class="text-center" id="usuario">
        <v-menu open-on-hover>
            <template v-slot:activator="{ props }">
                <div v-bind="props">
                    <v-avatar image="../../../public/planeta.png" size="40"></v-avatar>{{ user.usuario }}
                </div>
            </template>

            <v-list>
                <v-list-item>
                    <v-list-item-title>
                        <a href @click.prevent="configuracao">

                            <svg-icon type="mdi" :path="mdiAccountEdit"></svg-icon> Configurações

                        </a>
                    </v-list-item-title>
                    <v-list-item-title>
                        <a href @click.prevent="logout">

                            <svg-icon type="mdi" :path="mdiLogout"></svg-icon> Sair

                        </a>
                    </v-list-item-title>
                </v-list-item>
            </v-list>
        </v-menu>
    </div>
</template>

<script setup>

import { storeToRefs } from 'pinia'
import { useUserStore } from '@/stores/user.js'
import { mdiAccountEdit, mdiLogout } from '@mdi/js'
import { userKey } from '@/global.js'
import { useRouter } from 'vue-router'


const useUser = useUserStore()
const { user } = storeToRefs(useUserStore())
const router = useRouter()


function configuracao() {

}

function logout() {

    localStorage.removeItem(userKey)
    useUser.setUser(null)
    router.push({ name: 'login' })

}

</script>

<style scoped>
#usuario {

    display: flex;
    align-items: center;
    margin-right: 100px;
    color: rgb(244, 236, 236);

}

a {

    text-decoration: none;
    color: rgb(94, 93, 93);
}
</style>