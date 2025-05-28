<template>
    <v-container>
        <div class="d-flex ml-5">
            <div style="margin-top: 40px">

                <div class="text-overline" v-for="(nivelLixo, index) in legendaEixoVerticalNiveisLixo" :key="index"
                    style="margin-bottom: 30px;">
                    {{ nivelLixo }}
                </div>

            </div>
            <v-sparkline :fill="fill" :gradient="selecionarGradiente" :line-width="lineWidth"
                :model-value="dadosGrafico" :padding="padding" :smooth="smooth" auto-draw :height="100"
                style="margin-left: 80px;"></v-sparkline>

        </div>
        <div class="justify-space-between d-flex">

            <div class="text-overline mb-1" style="font-size: 8px !important;"
                v-for="(legenda, index) in legendaInferiorEixoX" :key="index">
                {{ legenda }}
            </div>
        </div>
    </v-container>
</template>
<script setup>
import { ref, watch } from 'vue'
import { storeToRefs } from 'pinia'

import { useInformativoLixeiraStore } from '../../../stores/informativoLixeira.js'

const informativoLixeiraStore = useInformativoLixeiraStore()
const { informativosLixeira } = storeToRefs(informativoLixeiraStore)

const legendaInferiorEixoX = ref([])
const legendaEixoVerticalNiveisLixo = ['100%', '75%', '50%', '25%', '0%']
const dadosGrafico = ref([])

const gradientes = [
    ['red', 'yellow', 'green']
]
const fill = ref(false)
const selecionarGradiente = ref(gradientes[0])
const padding = ref(0)
const smooth = ref(true)
const lineWidth = ref(0.5)

function atualizarLegendaInferiorEixoX() {
    const primeirasDatas = informativosLixeira.value.slice(0, 10).reverse()
    console.log(primeirasDatas);
    const datas = primeirasDatas.map((informativo) => new Date(informativo.criado_em).toLocaleString().split(" ")[0])
    const diaMes = datas.map((data) => data.split("/")).map((dd) => `${dd[0]}/${dd[1]}`)
    diaMes.unshift('Nivel Lixeira')
    legendaInferiorEixoX.value = diaMes
}

function atualizarDados() {

    dadosGrafico.value = informativosLixeira.value.map((informativo) => informativo.nivel_lixeira).slice(0, 10).reverse()

}


//Monitora as mudanças do informativo
watch(informativosLixeira.value, (newValue) => {
    atualizarLegendaInferiorEixoX()
    atualizarDados()
})

atualizarLegendaInferiorEixoX()
atualizarDados()


</script>
<style scoped>
.switch {
    position: relative;
    top: -12px;
}
</style>