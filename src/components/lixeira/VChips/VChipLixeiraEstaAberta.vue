<script setup>

import { mdiDeleteEmpty, mdiDelete } from '@mdi/js';
import { storeToRefs } from 'pinia'
import { useLixeiraStore } from '@/stores/lixeira'
const lixeiraStore = useLixeiraStore()
const { lixeira } = storeToRefs(lixeiraStore)

</script>
<template>
    <v-chip :color="lixeira.esta_aberta == 'Aberta' ? 'white' : 'white'">
        <svg-icon type="mdi" :path="lixeira.esta_aberta == 'Aberta' ? mdiDeleteEmpty : mdiDelete"></svg-icon>
        {{
            lixeira.esta_aberta }}</v-chip>
</template>