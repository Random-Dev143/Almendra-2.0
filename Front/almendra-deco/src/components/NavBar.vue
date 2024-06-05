<template>
    <header>
      <nav>
        <div class="nav-container">
          <font-awesome-icon 
            icon="bars" 
            class="menu-icon" 
            @click="toggleMenu" 
            v-if="!isMenuOpen && !isTransitioning"
          />
          <div class="links" :class="{ show: isMenuOpen, hide: !isMenuOpen && isTransitioning }" @transitionend="handleTransitionEnd">
            <RouterLink class="link" to="/" @click="closeMenu">Home</RouterLink>
            <RouterLink class="link" to="/login" @click="closeMenu">Login</RouterLink>
            <RouterLink class="link" to="/about" @click="closeMenu">About</RouterLink>
          </div>
        </div>
      </nav>
    </header>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue';
  
  const isMenuOpen = ref(false);
  const isTransitioning = ref(false);
  
  function toggleMenu() {
    isMenuOpen.value = !isMenuOpen.value;
    isTransitioning.value = true;
  }
  
  function closeMenu() {
    isMenuOpen.value = false;
    isTransitioning.value = true;
  }
  
  function handleTransitionEnd() {
    if (!isMenuOpen.value) {
      isTransitioning.value = false;
    }
  }
  </script>
  
  <style scoped>
  header {
    box-shadow: 0px 1px 4px 0px rgba(0, 0, 0, 0.25);
  }
  
  nav {
    padding: 15px 0;
    width: 100%;
    background-color: rgba(217, 217, 217, 1);
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .nav-container {
    display: flex;
    padding-left: 15px;
    justify-content: space-between;
    align-items: center;
    width: 100%;
  }
  
  .menu-icon {
    display: none;
    font-size: 24px;
    cursor: pointer;
    color: rgba(66, 66, 66, 1);
  }
  
  .links {
    display: flex;
    transition: max-height 0.3s ease-in-out, opacity 0.3s ease-in-out;
    max-height: 0;
    opacity: 0;
    overflow: hidden;
    flex-direction: column;
    align-items: center;
    width: 100%;
  }
  
  .links.show {
    max-height: 500px; /* Ajustar según la cantidad de enlaces */
    opacity: 1;
  }
  
  .links.hide {
    max-height: 0;
    opacity: 0;
  }
  
  .link {
    margin: 10px 0;
    padding: 10px;
    text-decoration: none;
    color: rgba(66, 66, 66, 1);
    width: 100%;
    text-align: center;
  }
  
  .link:hover {
    background-color: #555;
  }
  
  @media (max-width: 768px) {
    .menu-icon {
      display: block;
    }
  
    .links {
      display: flex;
    }
  
    .link {
      width: 100%;
    }
  }
  
  @media (min-width: 769px) {
    .links {
      flex-direction: row;
      max-height: none;
      opacity: 1;
      transition: none;
    }
  
    .link {
      margin: 0 10px;
      padding: 10px;
    }
  }
  </style>
  