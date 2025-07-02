<script setup lang="ts">

import { mdiTruck } from '@mdi/js'

defineProps({

    configuracaoTitulo: {
        type: Object,
        required: true
    }
})

</script>

<template>

    <v-toolbar-title>
        <svg-icon type="mdi" :path="configuracaoTitulo.icone"></svg-icon>
        <span style="color: var(--btn-text-color);">{{ configuracaoTitulo.nome }}</span>
    </v-toolbar-title>



</template>

<style scoped>
span {

    color: rgb(94, 93, 93);
}
</style>
