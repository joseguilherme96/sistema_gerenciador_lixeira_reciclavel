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


    <v-progress-linear v-cor-nivel-lixeira="item.nivel_lixeira" v-model:model-value="item.nivel_lixeira" :height="30">{{
        item.nivel_lixeira
    }}%</v-progress-linear>

</template>

<style scoped></style>
