<template>
  <div id="app">
    <NavBar />
    <RouterView />
  </div>
</template>

<script setup lang="ts">
import { RouterView } from 'vue-router';
import NavBar from '@/components/NavBar.vue';
</script>

<style>
html, body {
  font-family: 'Be Vietnam Pro', sans-serif;
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(217, 217, 217, 1);
  box-sizing: border-box;
}

:root{
  background-color:rgba(217, 217, 217, 1);
  width: 100%;
}
#navBar{
  position: sticky;
  z-index: 1;
  box-shadow: 0px 1px 4px 0px rgba(0, 0, 0, 0.25);
}



</style>
