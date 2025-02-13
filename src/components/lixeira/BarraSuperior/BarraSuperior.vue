<script setup lang="ts">

import TituloPagina from '../Titulo/TituloPagina.vue'

const emit = defineEmits(['abrirModalCadastroLixeira', 'abrirModalFiltro'])

function abrirModalCadastro() {

    emit('abrirModalCadastroLixeira', true)

}

function abrirModalFiltro() {


    emit('abrirModalFiltro', true)


}

</script>

<template>

    <v-toolbar class="mb-5">
        <TituloPagina></TituloPagina>
        <slot name="opcoes">
        </slot>
    </v-toolbar>


</template>

<style scoped>
span {

    color: rgb(94, 93, 93);
}
</style>
