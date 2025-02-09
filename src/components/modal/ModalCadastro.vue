<script setup lang="js">

defineProps({
    data: Object
})

</script>

<template>


<v-dialog v-model="data.exibir"max-width="900">
            <template v-slot:default="{ isActive }">

                <v-card>

                   <slot name="conteudo">
                   </slot>

                    <template v-slot:actions>
                    <slot name="botoes">
                    </slot>
                    </template>               
                
                </v-card>
            </template>
        </v-dialog>

</template>