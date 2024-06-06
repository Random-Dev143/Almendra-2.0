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
          <a class="link" href="/home">Home</a>
          <a class="link" href="/login">Login</a>
          <a class="link" href="/about">About</a>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
import { ref } from 'vue';

export default {
  name: 'NavBar',
  data() {
    return {
      isMenuOpen: false,
      isTransitioning: false
    };
  },
  methods: {
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
      this.isTransitioning = true;
    },
    closeMenu() {
      this.isMenuOpen = false;
      this.isTransitioning = true;
    },
    handleTransitionEnd() {
      if (!this.isMenuOpen) {
        this.isTransitioning = false;
      }
    }
  }
};
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
  