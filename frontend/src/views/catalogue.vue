<template>
    <div>
      <Header></Header>
      <div class="catalogue-grid">
        <div v-for="(item, index) in catalogue" :key="index" class="catalogue-item">
          <div class="item">
            <img :src="`../..${item.image}`" :alt="item.name" />
            <h3>{{ item.name }}</h3>
            <p>{{ item.price }}</p>
          </div>
        </div>
      </div>
      <Footer></Footer>
    </div>
  </template>
  
  <script>
  import Header from "./../components/header.vue";
  import Footer from "./../components/footer.vue";
  import axios from 'axios';
  
  export default {
    components: {
      Header,
      Footer
    },
    data() {
      return {
        catalogue: [] 
      };
    },
    mounted() {
      axios.get('http://127.0.0.1:5000/pals')
        .then(response => {
          this.catalogue = response.data; // Mettez à jour la liste de produits avec les données récupérées de l'API
        })
        .catch(error => {
          console.error('Erreur lors de la récupération des produits du catalogue', error);
        });
    }
  };
  </script>
  
  <style scoped>
  .catalogue-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr); /* Crée 4 colonnes de largeur égale */
    gap: 20px; /* Espace entre les éléments */
    padding: 20px;
  }
  
  .item {
    text-align: center;
    padding: 10px;
    border: 1px solid #ccc;
  }
  
  
    * {
        margin: 0;
        padding: 0;
        background-color:#FFEDE1;
    }

</style>