<template>
  <div>
    <Header></Header>
    <div v-if="pal" class="pal-page">
      <h1>Plus d'infos sur {{ pal.name }}</h1>
      <div class="pal-details">
        <div class="pal-info">
          <p><strong>Nom :</strong> {{ pal.name }}</p>
          <p><strong>Prix :</strong> {{ pal.price }}</p>
          <p><strong>Description :</strong> {{ pal.description }}</p>
          <p><strong>Utilité :</strong></p>
          <div class="suitability-icons">
            <img v-for="item in pal.suitability" :key="item.type" :src="item.image" :alt="item.type" class="suitability-icon">
          </div>
          <p><strong>Type : </strong></p>
          <div class="types">
            <img v-for="type in pal.types" :key="type" :src="`/images/elements/${type}.png`" :alt="type" class="type-icon">
          </div>
        </div>          
        <div class="pal-image">
          <img :src="pal.image" :alt="pal.name" style="display: block; margin: 0 auto;">
        </div>
      </div>
      <button @click="addToCart">Ajouter au panier</button>
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
      pal: null
    };
  },
  mounted() {
    const palId = this.$route.params.id;
    axios.get('https://palshopprojetvue.onrender.com/pals/' + palId) 
      .then(response => {
        this.pal = response.data; 
      })
      .catch(error => {
        console.error('Une erreur s\'est produite lors de la récupération des données du Pal', error);
      });
  },
  methods: {
    addToCart() {
      if (this.pal) {
        const cartItem = {
          id: this.pal.key,
          name: this.pal.name,
          price: this.pal.price,
          image: this.pal.image
        };
        let cartItems = JSON.parse(sessionStorage.getItem('cartItems')) || [];
        cartItems.push(cartItem);
        sessionStorage.setItem('cartItems', JSON.stringify(cartItems));
        this.$router.push('/panier');
      }
    }
  }
};
</script>
  
<style scoped>
* {
  margin: 0;
  padding: 0;
  background-color: #FFEDE1;
}

h1 {
  text-align: center; 
  color: #39487E; 
  font-size: 60px;
  margin-top: 20px;
}

.pal-page {
  min-height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  padding: 20px;
  button {
    padding: 1em;
    border-radius: 20px;
    border: 2px solid #819ECC;
    color: #819ECC;
    font-weight: 500;
    width: 30%;
    transition-duration: .3s;
  }
  button:hover{
    background-color: #819ECC;
    color: white;
  }
}

.pal-details {
  display: flex;
  justify-content: flex-end; 
  text-align: left; 
  margin-top: 10px;
  margin-bottom: 20px;
  width: 70%; 
}

.pal-info {
  margin-right: 20px;
  width: 45%; 
  margin-top: 10%;
  margin-left: 10px;
  h2 {
    color: #39487E;
    font-size: 30px;
    font-weight: 400;
  }
  p {
    color: #39487E;
    font-size: 20px;
  }
  .suitability-icons {
    img {
      margin-right: 5px;
    }
  }
  .type-icon{
    margin-right: 5px;
  }
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

@media only screen and (max-width: 1279px) {
  .pal-page {
    h1 {
      font-size: 30px;
    }
  }
  .pal-info {
    p {
      width: 90%;
      font-size: 14px;
    }
  }
}
</style>