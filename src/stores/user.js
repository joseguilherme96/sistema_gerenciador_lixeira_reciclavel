import { defineStore } from 'pinia'
import axios from 'axios'


export const useUserStore = defineStore('user', {

    state: () => ({

        user: null

    }),
    actions: {

        setUser(user) {

            this.user = user

            if (user) {

                axios.defaults.headers.common['Authorization'] = `Bearer ${user.token_acesso}`

            } else {

                delete axios.defaults.headers.common['Authorization']

            }

        }


    }

})