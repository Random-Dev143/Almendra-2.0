<template>
  <div class="filtros-bar">
    <ul class="categoria-lista">
      <li
        v-for="(categoria, index) in categorias"
        :key="index"
        :class="{ 'categoria-item': true, 'selected': isSelected(categoria) }"
        @click="toggleCategoria(categoria)"
      >
        {{ categoria }}
      </li>
      <li v-if="categoriasSeleccionadas.length > 0" class="categoria-item" @click="mostrarTodos">
        Todos
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'FiltrosBar',
  data() {
    return {
      categorias: [],
      categoriasSeleccionadas: [],
      url: 'http://localhost:5000/api/productos'
    };
  },
  mounted() {
    this.fetchCategorias();
  },
  methods: {
    async fetchCategorias() {
      try {
        const response = await fetch(this.url);
        if (!response.ok) {
          throw new Error(`Error al obtener productos. Código de estado: ${response.status}`);
        }
        const productos = await response.json();
        this.categorias = [...new Set(productos.map(producto => producto.categoria))];
      } catch (error) {
        console.error('Error al obtener productos:', error.message);
      }
    },
    toggleCategoria(categoria) {
      const index = this.categoriasSeleccionadas.indexOf(categoria);
      if (index === -1) {
        this.categoriasSeleccionadas.push(categoria);
        if (categoria === 'Todos' && this.categoriasSeleccionadas.length === 1) {
          this.categoriasSeleccionadas = [];
        }
      } else {
        this.categoriasSeleccionadas.splice(index, 1);
        if (categoria === 'Todos' && this.categoriasSeleccionadas.length === 0) {
          this.categoriasSeleccionadas = this.categorias.filter(cat => cat !== 'Todos');
        }
      }
      this.$emit('categorias-seleccionadas', this.categoriasSeleccionadas);
    },
    isSelected(categoria) {
      return this.categoriasSeleccionadas.includes(categoria);
    },
    mostrarTodos() {
      if (this.categoriasSeleccionadas.length > 0) {
        this.categoriasSeleccionadas = [];
        this.$emit('categorias-seleccionadas', this.categoriasSeleccionadas);
      }
    }
  }
};
</script>

<style scoped>
.filtros-bar {
  overflow-x: auto;
  white-space: nowrap;
}

.categoria-lista {
  display: flex;
  list-style: none;
  padding: 0;
  margin: 1rem 0;
}

.categoria-item {
  cursor: pointer;
  padding: 0.5rem 1rem;
  margin-right: 0.5rem;
  background: rgba(243, 239, 228, 1);
  color:black;
  border-radius: 4px;
  transition: background-color 0.3s;
  display: inline-block;
}

.categoria-item:hover {
  background: rgba(208, 156, 134, 1);
}

.selected {
  background: rgba(208, 156, 134, 1);
}

@media (max-width: 600px) {
  .categoria-item {
    font-size: 0.9rem;
  }

  .filtros-bar {
    height: 22px;
  }
}
</style>
