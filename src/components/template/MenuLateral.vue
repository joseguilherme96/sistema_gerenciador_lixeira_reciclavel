<template>

    <div class="menu-lateral">
        <ul>
            <li v-for="rota in rotas">
                <RouterLink :to="rota.path">{{ rota.liMenu }}</RouterLink>
            </li>
        </ul>
    </div>

</template>
<script setup>

import { useRouter } from 'vue-router';

const router = useRouter();
const rotas = router.getRoutes().map((item) => ({ ...item, liMenu: item.name.replaceAll('-', ' ') })).filter((item) => item.name != 'login')

</script>
<style scoped>
.menu-lateral {
    width: 20%;
    min-height: 100vh;
    background-color: var(--btn-bg-primary-color);
}

ul {
    margin-left: 10px;
}

li {
    color: white;
    margin-bottom: 5px;
}

a {
    color: white;
    text-decoration: none;
    text-transform: capitalize;
}
</style>