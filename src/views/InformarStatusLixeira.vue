<script setup lang="js">
import BarraSuperior from '@/components/lixeira/BarraSuperior/BarraSuperior.vue';
import TituloPagina from '@/components/lixeira/Titulo/TituloPagina.vue';
import { mdiInformation, mdiTruck } from '@mdi/js';

const configuracaoTitulo = {

    nome: 'Infomar Status Lixeira',
    icone: mdiInformation,

}

</script>

<template>


    <BarraSuperior>

        <template v-slot:titulo>

            <TituloPagina :configuracaoTitulo="configuracaoTitulo"></TituloPagina>

        </template>

    </BarraSuperior>


</template>