<script setup lang="js">

import { vCorNivelLixeira } from '../../../directives/cor.nivel.lixeira.diretiva.js';

defineProps({
    item: {
        type: Object,
        required: true
    }
})


</script>

<template>


    <v-progress-linear v-cor-nivel-lixeira="item.nivelLixeira" v-model:model-value="item.nivelLixeira" :height="30">{{
        item.nivelLixeira
        }}%</v-progress-linear>

</template>

<style scoped></style>
