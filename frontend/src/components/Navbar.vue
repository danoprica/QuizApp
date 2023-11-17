<template>
    <Menubar>
        <template #start>
            <div v-if="userStore.userName">{{ userStore.userName }}</div>
        </template>
        <template #end>
            <router-link to="/">Home</router-link>  |   
            <router-link to="/login">Login</router-link>
        </template>
    </Menubar>
</template>

<script setup>

import { useUser } from "../store/modules/user";
const userStore = useUser();


</script>