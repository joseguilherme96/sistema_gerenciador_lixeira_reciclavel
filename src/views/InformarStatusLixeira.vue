<script setup lang="js">
import BarraSuperior from '@/components/lixeira/BarraSuperior/BarraSuperior.vue';
import TituloPagina from '@/components/lixeira/Titulo/TituloPagina.vue';
import { mdiTruck } from '@mdi/js';

const configuracaoTitulo = {

    nome: 'Infomar Status Lixeira',
    icone:mdiTruck,

}

</script>

<template>

    <BarraSuperior>

        <template v-slot:titulo>

            <TituloPagina :configuracaoTitulo="configuracaoTitulo"></TituloPagina>

        </template>

    </BarraSuperior>
    
</template>