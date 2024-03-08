<template>
    <Header></Header>
    <h1>Panier</h1>
    <div class="cart-items">
        <div class="void-checkout" v-if="cartItems.length === 0">
            <p>Votre panier est vide.</p>
        </div>
        <div class="contain-checkout" v-else>
            <div v-for="(item, index) in cartItems" :key="index" class="cart-item">
                <img :src="item.image" :alt="item.name" style="width: 100px; height: 100px;">
                <h2>{{ item.name }}</h2>
                <p>Prix : {{ item.price }}</p>
                <button @click="removeFromCart(index)">Supprimer</button>
                <separator>.</separator>
            </div>
            <div class="total-price">
                <p id="price">Prix total : {{ getTotalPrice() }}</p>
            </div>
        </div>
        <button class="checkout" @click="checkout">Procéder au paiement</button>
    </div>
    <Footer></Footer>

</template>

<script>
    import Header from "./../components/header.vue";
    import Footer from "./../components/footer.vue";

    export default {
    components: {
        Header,
        Footer
    },
    data() {
        return {
        cartItems: []
        };
    },
    mounted() {
        this.getCartItemsFromSessionStorage();
    },
    methods: {
        getCartItemsFromSessionStorage() {
            const storedCartItems = sessionStorage.getItem('cartItems');
            if (storedCartItems) {
                this.cartItems = JSON.parse(storedCartItems);
            }
        },
        removeFromCart(index) {
            this.cartItems.splice(index, 1);
            sessionStorage.setItem('cartItems', JSON.stringify(this.cartItems));
        },
        getTotalPrice() {
            let totalPrice = 0;
            for (const item of this.cartItems) {
                totalPrice += parseFloat(item.price);
            }
            return totalPrice;
        },
        checkout() {
            this.cartItems = [];
            sessionStorage.removeItem('cartItems');
        }
    }
    };
</script>

<style scoped>
    *{
        padding: 0;
        margin: 0;
        background-color: #FFEDE1;
    }

    h1 {
        color: #39487E;
        font-size: 50px;
        text-align: center;
        padding-bottom: 30px;
    }

    p {
        font-weight: 500;
        color: #39487E;
    }

    .void-checkout {
        p {
            color: #39487E;
            font-size: 30px;
            text-align: center;
        }
    }
    .contain-checkout {
        div {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-evenly;
            h2 {
                margin: auto 0;
                width: 15%;
                color: #39487E;
            }
            p {
                margin: auto 0;
                width: 15%;
                font-size: 18px;
            }
            img {
                margin: auto 0;
                width: 15%;
                background-color: #819ECC;
                border-radius: 10px;
            }
            button {
                background-color: white;
                width: 10%;
                margin: auto 0;
                border: 3px solid #f76d6d;
                border-radius: 20px;
                padding: .3em;
                color: #f76d6d;
                font-size: 15px;
                transition-duration: .3s;
            }
            button:hover {
                color: white;
                background-color: #f76d6d;
            }
            separator {
                width: 80%;
                background-color: #39487E;
                font-size: 2px;
                margin: 10px 0;
            }
            
        }
        #price {
            text-align: center;
            padding: .8em 0;
        }
        
    }
    .checkout {
        display: flex;
        margin: auto;
        border: 3px solid #39487E;
        border-radius: 20px;
        padding: .55em;
        color: #39487E;
        font-size: 15px;
        transition-duration: .3s;
    }
    .checkout:hover {
        color: white;
        background-color: #39487E;
    }

    @media only screen and (max-width: 1279px) {
    .contain-checkout {
        div {
            h2 {
                font-size: 14px;
            }
            p{
                font-size: 12px;
            }
            button {
                width: 25%;
            }
        }
    }
    #price {
        width: 50%;
    }
    
    }

</style>