<template>
  <div class="login-container">
    <h1>Bienvenido a Almendra Decoraciones</h1>
    <div class="login-card">
      <h2>Iniciar Sesión</h2>
      <form @submit.prevent="handleLogin">
        <div class="input-group">
          <label for="username">Usuario</label>
          <input type="text" id="username" v-model="username" required />
        </div>
        <div class="input-group">
          <label for="password">Contraseña</label>
          <input type="password" id="password" v-model="password" required />
          <div v-if="loginError" class="error-message">{{ loginErrorMessage }}</div>
        </div>
        <button type="submit">Iniciar Sesión</button>
      </form>
      <div class="links">
        <a href="#" @click.prevent="handleRegister">Registrarse</a>
        <br>
        <a href="#" @click.prevent="handleRecoverPassword">Recuperar Contraseña</a>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { useRouter } from 'vue-router';

export default {
    data() {
    return {
      username: '',
      password: '',
      loginError: false,
      loginErrorMessage: ''
    };
  },
  methods: {
    async handleLogin() {
  try {
    const response = await axios.post('http://localhost:5000/api/auth/login', {
      email: this.username,
      password: this.password
    });
    console.log(response.data);
    if (response.data.access_token) {
      // Redirige al usuario a la página de inicio después de iniciar sesión
      window.location.href = '/home'; // Cambia '/home' por la ruta real de tu página de inicio
    }
  } catch (error) {
    console.error(error);
    if (error.response.status === 401) {
      const message = error.response.data.error;
      if (message === 'Invalid credentials') {
        this.loginError = true;
        this.loginErrorMessage = 'Usuario o contraseña incorrectos';
      } else {
        this.loginError = false; 
        this.loginErrorMessage = '';
        alert('Usuario no encontrado');
      }
    }
  }
},

    handleRegister() {
      // Lógica para registrarse
    },
    handleRecoverPassword() {
      // Lógica para recuperar contraseña
    }
  }
}
</script>

<style scoped>
  .error-message {
    color: red;
    margin-top: 5px;
    font-size: 0.8rem;
  }
  .login-container {
    background-color: rgba(217, 217, 217, 1);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    height: 100vh;
    padding: 20px;
  }
  
  h1 {
    margin: 15px;
    color: #333;
    text-align: center;
  }
  
  .login-card {
    background: rgba(243, 239, 228, 1);
    padding: 20px;
    border-radius: 5%;
    box-shadow: 0px 3px 11.9px 0px rgba(0, 0, 0, 0.25);
    width: 100%;
    max-width: 400px;
    box-sizing: border-box;
  }
  
  h2 {
    margin-bottom: 20px;
    color: #555;
    text-align: center;
  }
  
  .input-group {
    margin-bottom: 15px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
    color: #666;
  }
  
  input {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
    border: 1px solid #ddd;
    background: rgba(255, 255, 255, 1);
    border-radius: 4px;
  }
  
  button {
    width: 100%;
    padding: 10px;
    background-color: rgba(208, 156, 134, 1);
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #b35a40;
  }
  
  .links {
    margin-top: 15px;
    text-align: center;
  }
  
  .links a {
    color: #007bff;
    text-decoration: none;
    margin: 0 10px;
  }
  
  .links a:hover {
    text-decoration: underline;
  }
  
  
  @media (max-width: 768px) {
    .login-container {
      padding: 10px;
    }
  
    .login-card {
      padding: 15px;
    }
  
    h1 {
      font-size: 1.5rem;
    }
  
    h2 {
      font-size: 1.2rem;
    }
  
    button {
      padding: 8px;
    }
  }
  
  @media (max-width: 480px) {
    .login-container {
      padding: 15px;
    }
  
    .login-card {
      padding: 15px;
    }
  
    h1 {
      font-size: 1.2rem;
    }
  
    h2 {
      font-size: 1rem;
    }
  
    button {
      padding: 6px;
    }
  }
  </style>
  