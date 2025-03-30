<script setup lang="js">


import QRious from 'qrious';
import { ref, watch, watchEffect } from 'vue';

const props = defineProps({

    configuracaoQRCode: {
        type: Object
    }

})

watch(() => props.configuracaoQRCode, (newVal) => {

    console.log(newVal)

})


const qrCanvas = ref(null)

const editarTamanhoQRCode = () => {
    qrCanvas.value.style.width = `${props.configuracaoQRCode.width}px`;
    qrCanvas.value.style.height = `${props.configuracaoQRCode.height}px`;
}

const criarQRCode = () => {
    var qr = new QRious({
        element: qrCanvas.value
    });

    qr.padding = 20;
    qr.size = 500;
    qr.value = props.configuracaoQRCode.valor;
}

watch(() => qrCanvas.value, (newVal) => {

    editarTamanhoQRCode();

    criarQRCode();
})

</script>

<template>

    <canvas ref="qrCanvas"></canvas>

</template>