<template>
  <div>
    <Header></Header>
    <h1>CATALOGUE</h1>
    <div class="filter-section">
      <input v-model="searchName" type="text" placeholder="Rechercher par nom">
    </div>
    <h2>NOS PAL DISPONIBLE</h2>
    <div class="catalogue-grid">
      <router-link v-for="(item, index) in catalogue" :key="index" :to="`/pal/${index}`" class="catalogue-item" v-show="matchesFilters(item)">
        <div class="item">
          <img :src="`../..${item.image}`" :alt="item.name" />
          <h3>{{ item.name }}</h3>
          <p>{{ item.price }} <font-awesome-icon :icon="['fas', 'shopping-cart']" /></p>
        </div>
      </router-link>
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
      catalogue: [],
      searchName: '',
      searchPrice: null
    };
  },
  mounted() {
    axios.get('https://palshopprojetvue.onrender.com/pals')
      .then(response => {
        this.catalogue = response.data;
      })
      .catch(error => {
        console.error('Erreur lors de la récupération des produits du catalogue', error);
      });
  },
  methods: {
    applyFilters() {
      this.filteredCatalogue = this.filterCatalogue();
    },
    filterCatalogue() {
      return this.catalogue.filter(item => {
        let nameMatch = true;
        if (this.searchName) {
          nameMatch = item.name.toLowerCase().includes(this.searchName.toLowerCase());
        }
        let priceMatch = true;
        if (this.searchPrice !== null) {
          priceMatch = item.price <= this.searchPrice;
        }
        return nameMatch && priceMatch;
      });
    },
    matchesFilters(item) {
      if ((this.searchName && !item.name.toLowerCase().includes(this.searchName.toLowerCase())) ||
          (this.searchPrice !== null && item.price > this.searchPrice)) {
        return false; 
      }
      return true; 
    },
    updatePriceValue(event) {
      this.searchPrice = event.target.value;
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
  h2 {
    color: #39487E;
    font-size: 40px;
    margin-left: 50px;
  }
  
  .filter-section {
    input {
      border: 3px solid #819ECC
    }
  }
  .catalogue-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr); 
    gap: 20px;
    padding: 20px;
    a {
      text-decoration: none;
      font-size: 20px;
      color: #39487E;
    }
  }

  .item {
    text-align: center;
    padding: 10px;
    border: none;
    max-width: 100%;
  }

  .item img {
    max-width: 80%; 
    height: auto;
    border-radius: 10px; 
    box-shadow: 1px 5px 20px rgb(72, 72, 72);
    transition-duration: .3s;    
    background-color: #819ECC;
  }
  .item img:hover {
    box-shadow: 1px 5px 20px rgb(0, 0, 0);
  }    



  .filter-section {
    margin: 20px auto;
    width: 30%; 
    text-align: center;
    padding: 20px; 
  }

  .filter-section input {
    width: 80%; 
    padding: 10px; 
    margin-bottom: 10px; 
    background-color: white;
  }
</style>
