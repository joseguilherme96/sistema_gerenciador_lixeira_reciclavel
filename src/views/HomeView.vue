<script setup lang="js">
import TheWelcome from '../components/TheWelcome.vue'

import { useUserStore } from "@/stores/user.js"
import { storeToRefs } from 'pinia';

const useUser = useUserStore()
const { user } = storeToRefs(useUserStore())

</script>

<template>
  <main>
  </main>
</template>
