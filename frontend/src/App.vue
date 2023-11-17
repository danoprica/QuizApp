<template>
  <Navbar />
  <div class="main-wrapper">
    <div class="main-container">
      <router-view />
    </div>
  </div>
  <Footer />
</template>

<script setup>

import Navbar from "./components/Navbar.vue";
import Footer from "./components/Footer.vue";

</script>


