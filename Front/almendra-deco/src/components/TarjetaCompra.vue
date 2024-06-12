<template>
  <div style="margin: 0 0.5rem;">
    <filtros-bar @categorias-seleccionadas="aplicarFiltrosCategorias" @destacados-seleccionado="aplicarFiltroDestacados" style="margin-bottom: 1.5rem;" />
    <div class="card-grid" style="margin-bottom: 3rem;">
      <div v-for="(producto, index) in productosFiltrados" :key="index" class="card">
        <div class="card-body">
          <div class="carousel-container">
            <div class="carousel" :id="'carousel-' + producto.id" :style="{ transform: `translateX(-${currentIndex[producto.id] * 100}%)` }">
              <div class="carousel-slide" v-for="(imagen, imgIndex) in producto.imagenes" :key="`imagen-${producto.id}-${imgIndex}`">
                <img :src="imagen.url" class="carousel-img" :alt="`Imagen ${imgIndex + 1}`" />
              </div>
            </div>
            <button v-if="producto.imagenes.length > 1" class="prev" @click="prevSlide(producto.id)">&#10094;</button>
            <button v-if="producto.imagenes.length > 1" class="next" @click="nextSlide(producto.id)">&#10095;</button>
          </div>
          <div class="datos-productos">
            <p class="card-categoria">{{ producto.categoria }}</p>
            <h5 class="card-title">{{ producto.nombre }}</h5>
            <p class="card-text descripcion">{{ producto.descripcion }}</p>
            <p class="card-text"><strong>${{ producto.precio }}</strong></p>
            <div class="btn-container">
              <div href="#" class="btn ver-btn" @click.prevent="emitirInfoProducto(producto.id)">
                <span class="material-symbols-outlined">info</span>
              </div>              
              <div href="#" class="btn agregar-btn" @click.prevent="agregarCarro(producto.id)">
                <span class="material-symbols-outlined">add_shopping_cart</span>              
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


  
<script>
import FiltrosBar from './FiltrosBar.vue';

export default {
  name: 'TarjetasCompras',
  components: {
    FiltrosBar,
  },
  props: {
    category: {
      type: String,
      default: ''
    }
  },
  data() {
    return {
      productos: [],
      productosFiltrados: [],
      currentIndex: {},
      url: 'http://localhost:5000/api/productos'
    };
  },
  mounted() {
    console.log('Prop "category" recibido:', this.category);
    this.fetchProductos();
  },
  methods: {
    async fetchProductos() {
      try {
        const response = await fetch(this.url);
        if (!response.ok) {
          throw new Error(`Error al obtener productos. Código de estado: ${response.status}`);
        }
        const data = await response.json();
        this.productos = data;
        this.productos.forEach(producto => {
          this.currentIndex[producto.id] = 0;
        });
        this.aplicarFiltros(this.category ? [this.category] : []);
      } catch (error) {
        console.error('Error al obtener productos:', error.message);
      }
    },
    aplicarFiltros(categorias) {
      if (categorias.length === 0) {
        this.productosFiltrados = this.productos;
      } else {
        this.productosFiltrados = this.productos.filter(producto => categorias.includes(producto.categoria));
      }
    },
    aplicarFiltrosCategorias(categorias) {
      this.aplicarFiltros(categorias);
    },
    aplicarFiltroDestacados() {
      this.productosFiltrados = this.productos.filter(producto => producto.destacado);
    },
    emitirInfoProducto(id) {
      this.$emit('producto-seleccionado', id);
      //console.log(id);
    },
    agregarCarro(id) {
      this.$emit('agregar-carrito', id); 
      //console.log(id)
    },
    prevSlide(productId) {
      if (this.currentIndex[productId] > 0) {
        this.currentIndex[productId]--;
      }
    },
    nextSlide(productId) {
      const maxIndex = this.productos.find(producto => producto.id === productId).imagenes.length - 1;
      if (this.currentIndex[productId] < maxIndex) {
        this.currentIndex[productId]++;
      }
    }
  }
};
</script>

<style scoped>
.card-grid {
  display: grid;
  justify-items: center;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  margin: 1.5rem;
}

.card {
  display: block;
  flex-grow: 1;
  flex-shrink: 0;
  height: 418px;
  max-width: inherit;
  width: 100%;
  z-index: 0;
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  max-width: 284px;
  background: rgba(243, 239, 228, 1);
  transition: transform 0.9s ease;
}

.card-body {
  padding: 1rem;
  min-height: 204px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
}


.carousel-container {
  position: relative;
  overflow: hidden;
  height: 214px;
  width: 100%;
  display: flex;
  align-items: center;
  border-radius: 8px;
}

.carousel {
  display: flex;
  transition: transform 0.5s ease;
}

.carousel-slide {
  min-width: 100%;
  height: 214px;
  box-sizing: border-box;
  display: flex;
  align-items: center; 
  justify-content: center; 
}

.carousel-img {
  max-width: 100%;
  max-height: 100%;
  width: auto;
  height: 100%;
  object-fit: cover;
  object-position: center;
  border-radius: 8px;
}

.prev, .next {
  cursor: pointer;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: auto;
  height: 100%;
  padding: 16px;
  color: rgba(255, 255, 255, 0.959);
  background-color: #6666661c;
  font-weight: bold;
  font-size: 18px;
  transition: 0.6s ease;
  border-radius: 0 3px 3px 0;
  user-select: none;
  border: none;
}

.next {
  right: 0;
  border-radius: 3px 0 0 3px;
}

.prev {
  left: 0;
  border-radius: 3px 0 0 3px;
}

.prev:hover, .next:hover {
  background-color: #11111167;
}

.datos-productos{
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}
.card-categoria {
  font-size: clamp(0.75rem, 1vw, 1rem);
  color: #666;
  margin: 0.2rem 0;
}

.card-title {
  font-size: clamp(0.90rem, 1.5vw, 1.2rem);
  font-weight: bold;
  margin: 0.2rem 0;
}

.card-text {
  font-size: clamp(0.775rem, 1.1vw, 0.875rem);
  margin-bottom: 0.5rem;
  margin: 0.2rem 0;
  align-self: center;
}

.card-text strong {
  font-size: clamp(1rem, 3vw, 20px);
  font-weight: 800;

}

.descripcion {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
  margin: 0.2rem 0;
}

.btn-container {
  display: flex;
  justify-content: space-between;
  width: 100%;
}

.btn {
  display: inline-block;
  padding: 0.5rem 1rem;
  font-size: clamp(0.75rem, 1vw, 1rem);
  border-radius: 8px;
  border: none;
  text-decoration: none;
  margin: 5px;
  flex: 1;
  text-align: center;
  max-width: 45%;
  cursor: pointer;
}

.ver-btn {
  background: rgba(224, 207, 162, 1);
  
}

.ver-btn:hover{
  background:  rgb(223, 197, 127) ;
}

.agregar-btn {
  background: rgba(208, 156, 134, 1);
}

.agregar-btn:hover{
  background: rgb(206, 132, 100);
}

.material-symbols-outlined {
  color: black;
  cursor: pointer;
  font-variation-settings:
  'FILL' 0.2,
  'wght' 800,
  'GRAD' 0,
  'opsz' 20,
}


@media (max-width: 600px) {
  .card-grid {
    grid-template-columns: repeat(auto-fit, minmax(161px, 1fr));
  }

  .card {
    height: 243px;
    width: 161px;
    border-radius: 40px 40px 40px 0;
  }

  .carousel-container {
    height: 139px;
    width: 142px;
    border-radius: 32px 32px 32px 0;
    outline: solid 5px rgba(244,207,162,1);
    overflow: hidden;
    margin-bottom: 5px;
  }

  .carousel-slide {
    height: 139px;
  }

  .carousel-img {
    height: 139px;
    width: auto;
    max-width: 100%;
    object-fit: cover;
    object-position: center;
    border-radius: 27px 27px 27px 0;
  }

  .card-body {
    padding: 0.5rem;
  }

  .card-categoria,
  .card-title,
  .card-text {
    margin: 0;
  }

  .card-title {
    font-size: 14px;
  }

  .card-text {
    font-size: 12px;
  }

  .descripcion {
    display: none;
  }

  .prev, .next {
    padding: 0 5px;
  }

  .btn-container {
    display: none;
  }
}
</style>

