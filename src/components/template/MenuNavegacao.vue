<script setup lang="js">

import { ref } from 'vue'
import UserDropdown from './UserDropdown.vue';
import { mdiMenu } from '@mdi/js';
import { useUserStore } from '../../stores/user.js'
import { storeToRefs } from 'pinia';
import { useRouter } from 'vue-router';

const router = useRouter();


const { exibirMenuLateral, user } = storeToRefs(useUserStore())

const items = ref([
    { title: 'Home', route: '/home' },
    { title: 'Sobre', route: '/about' },
    { title: 'Lixeiras', route: '/lixeiras' },
    { title: 'Relatório', route: '/relatorio-lixeira' }
])
</script>

<template>
    <!-- <div class="menu d-flex justify-space-between align-center">
        <div class="items">
            <div v-for="item in items" :key="item.route" class="item">
                <RouterLink :to="item.route">{{ item.title }}</RouterLink>
            </div>
        </div>
        <UserDropdown v-if="user"></UserDropdown>
    </div> -->
    <div class="menu d-flex justify-space-between align-center">
        <svg-icon type="mdi" :path="mdiMenu" class="item" size="40" color="rgb(255, 255, 255)"
            @click="exibirMenuLateral = !exibirMenuLateral"></svg-icon>
        <UserDropdown></UserDropdown>
    </div>
</template>

<style scoped>
a {
    text-decoration: none;
    color: rgb(255, 255, 255);
    padding: 10px 15px;
    display: block;
}

.items {
    display: flex;
    padding: 5px;
    transition: background-color 0.3s ease-in-out;
}

.item:hover {
    background-color: gray;
    color: red;
}


a:hover {
    color: white;
}


.menu {
    display: flex;
    justify-content: space-between;
    width: 100%;
    height: 60px;
    max-width: 2000px;
    background-color: var(--btn-bg-primary-color);
}
</style>
