<template>
  <div>
    <Header></Header>
    <h1 style="text-align: center; color: #819ECC;">Détails du Pal</h1>
    <div v-if="pal" class="pal-page">
      <div class="pal-details">
        <div class="pal-info">
          <h2>Nom: {{ pal.name }}</h2>
          <p>Prix: {{ pal.price }}</p>
        </div>
        <div class="pal-image">
          <img :src="pal.image" :alt="pal.name" style="display: block; margin: 0 auto;">
        </div>
      </div>
    </div>
    <Footer></Footer>
  </div>
</template>

  
  <script>
  import Header from "./../components/header.vue";
  import Footer from "./../components/footer.vue";
  import axios from "axios";
  
  export default {
    components: {
      Header,
      Footer
    },
    data() {
      return {
        palData: []
      };
    },
    created() {
      const palKey = this.$route.params.key;

      axios.get(`http://127.0.0.1:5000/pals/${palKey}`)
        .then(response => {
          console.log('Données du PAL récupérées avec succès', response.data);
          this.palData = response.data;
          console.log(response.data);
        })
        .catch(error => {
          console.error('Erreur lors de la récupération des données du PAL', error);
        });
    }
  }
  </script>
  
  <style scoped>
    * {
      margin: 0;
      padding: 0;
      background-color: #FFEDE1;
    }
  
  .pal-page {
    min-height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    padding: 20px;
  }
  
  .pal-details {
    display: flex; 
    align-items: center; 
    text-align: left;
    margin-bottom: 20px;
  }
  
  .pal-info {
    margin-right: 20px; 
    margin-left: 20px;
  }
  
  .pal-image {
    order: -1;
  }
  
  img {
    max-width: 100%;
    border-radius: 10px; 
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); 
    background-color: #819ECC;
  }
  </style>