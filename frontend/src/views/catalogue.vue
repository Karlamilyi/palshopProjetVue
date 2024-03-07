
<template>
  <div>
    <Header></Header>
    <div class="filter-section">
      <input v-model="searchName" type="text" placeholder="Rechercher par nom">
      <br>
      <input v-model="searchPrice" type="range" min="1000" max="10520" id="priceRange" @input="updatePriceValue">
      <span>{{ searchPrice }}</span>

    </div>
    <div class="catalogue-grid">
      <div v-for="(item, index) in catalogue" :key="index" class="catalogue-item" v-show="matchesFilters(item)">
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
      catalogue: [],
      searchName: '',
      searchPrice: null
    };
  },
  mounted() {
    axios.get('http://127.0.0.1:5000/pals')
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
.catalogue-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  padding: 20px;
}

.item {
  text-align: center;
  padding: 10px;
  border: 1px solid #ccc;
}

.filter-section {
  margin: 20px 0;
}

* {
  margin: 0;
  padding: 0;
  background-color: #FFEDE1;
}
</style>