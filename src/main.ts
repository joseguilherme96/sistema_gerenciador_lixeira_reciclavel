import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import '@mdi/font/css/materialdesignicons.css'

import SvgIcon from '@jamescoyle/vue-icon'

import '@/css/default.css'

import App from './App.vue'
import router from './router'

// Translations provided by Vuetify
import { pt } from 'vuetify/locale'

//Config
import './config/interceptacao.axios'

//Socket
import './services/socket.service'

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(createVuetify({
  components,
  directives,
  locale: {
    locale: 'pt',
    fallback: 'pt',
    messages: { pt },
  },
}))

app.component('svg-icon', SvgIcon)


app.mount('#app')
