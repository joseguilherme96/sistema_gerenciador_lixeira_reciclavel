<script setup lang="js">
import { ref } from 'vue'

const items = ref([
    { title: 'Home', route: '/' },
    { title: 'Sobre', route: '/about' },
    { title: 'Lixeiras', route: '/lixeiras' },
])
</script>

<template>
    <div class="menu">
        <div v-for="item in items" :key="item.route" class="item">
            <RouterLink :to="item.route">{{ item.title }}</RouterLink>
        </div>
    </div>
</template>

<style scoped>
a {
    text-decoration: none;
    color: rgb(94, 93, 93);
    padding: 10px 15px;
    display: block;
}

.item {
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
    justify-content: start;
    width: 100%;
    max-width: 2000px;
    margin-bottom: 10px;
}
</style>
