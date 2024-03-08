<template>
    <header>
        <div class="navbar-container">
            <div class="navbar">
                <a href="/"><h1>PALSHOP</h1></a>
                <ul>
                    <a href='/catalogue'>Catalogue</a>
                    <a href='/panier'>Panier</a>
                    <a id="connexion" href='/signup' v-if="loggedIn" @click="logout">Déconnexion</a>
                    <a id="connexion" href='/signup' v-else @click="showLoginModal">Connexion / Inscription</a>
                </ul>
            </div>
        </div>

        
    </header>
</template>

<script>
    export default {
    data() {
        return {
        loggedIn: localStorage.getItem('loggedIn') === 'true'
        };
    },
    methods: {
        logout() {
        localStorage.removeItem('loggedIn');
        this.loggedIn = false;
        },
        showLoginModal() {
        }
    }
    };

</script>

<style scoped>
    * {
        margin: 0;
        padding: 0;
        font-family: "Poppins", sans-serif;
        color: white;
    }
    .navbar-container {
        display: flex;
        flex-wrap: wrap;
        background-color: #39487E;
        margin: auto;
    }
    .navbar {
        margin: auto;
        width: 100%;
        max-width: 1280px;
        display: flex;
        flex-wrap: wrap;
        padding: 0.8em;
        a{
            text-decoration: none;
        }
        h1 {
            font-weight: 900;
        }
        ul {
            margin: auto 0 auto 50px;
            display: flex;
            a {
                font-weight: 200;
                text-decoration: none;
                margin: 0 50px 0 20px;
                transition: ease-in-out;
                transition-duration: 0.3s;
            }
            #connexion {
                margin-left: 500px;
            }

            a:hover{
                color: #FFEDE1;
                transform: scale(1.1);
                text-decoration: underline;
                font-weight: 400;
                /* ease in n out with a cubic bezier*/
                transition: cubic-bezier(0.215, 0.61, 0.355, 1) 0.3s;


            }
        }
    }

    @media only screen and (max-width: 1279px) {
        .navbar-container {
            .navbar {
                
                ul {
                    margin: 0;
                    a {
                        margin: 10px;
                   }
                    #connexion {
                        margin-left: 0px;
                    }
                }
            }
        }
        
        
    
    }
</style>