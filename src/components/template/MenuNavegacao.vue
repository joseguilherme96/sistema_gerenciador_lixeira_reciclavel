<script setup lang="js">

import { ref } from 'vue'
import UserDropdown from './UserDropdown.vue';

const items = ref([
    { title: 'Home', route: '/home' },
    { title: 'Sobre', route: '/about' },
    { title: 'Lixeiras', route: '/lixeiras' },
    { title: 'Relatório', route: '/relatorio-lixeira' }
])
</script>

<template>
    <div class="menu d-flex justify-end">
        <div class="items">
            <div v-for="item in items" :key="item.route" class="item">
                <RouterLink :to="item.route">{{ item.title }}</RouterLink>
            </div>
        </div>
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
    margin-bottom: 10px;
    background-color: var(--btn-bg-primary-color);
}
</style>
