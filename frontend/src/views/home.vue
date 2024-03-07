<template>
    <Header></Header>
    <div class="presentation-container">
        <h1>PALSHOP</h1>
        <h2><strong>C</strong>liquez, <strong>A</strong>chetez, <strong>D</strong>ominez</h2>
    </div>

    <div class="selection-container">
        <div class="selection">
            <h2>Les pals du moment</h2>
            <div v-for="(item, key) in items" :key="key">
                <img :src="item.image"/>
            </div>
            <a href="/Catalogue">En découvrir plus</a>
        </div>
    </div>

    <div class="moreinfos-container">
        <div class="moreinfos">
            <h2>Trois passionnés cherchant à révolutionner le marché</h2>
            <div class="leftside">
                <h3>"Des pals chez vous, au plus vite, au moins cher"</h3>
                <p>Avec ce projet, l’objectif est de créer un moyen complètement nouveau pour les dresseurs d’entreprendre leur aventure, pour vivre une expérience bien plus prenante.</p>
            </div>
            <img src="../../public/img/bg2homepage.jpg">
        </div>
    </div>

    <div class="catalogue-button-container">
        <div class="catalogue-button">
            <h2>Découvrez toute notre sélection de pals →</h2>
            <a href="Catalogue">Notre catalogue</a>
        </div>
    </div>

    <div class="contact-form-container">
        <h2>Une question ? Une réclamation ? C'est ici que ca se passe</h2>
        <div class="contact-infos">
            <h3>Informations de contact</h3> 
            <h4><strong>Adresse mail : </strong>contact@palshop.fr</h4>
            <h4><strong>Numéro : </strong>01.XX.XX.XX.XX</h4>

        </div>
        <div class="separator"></div>
        <div class="contact-form">
            <form>
                <input type="email" id="email" required placeholder="Votre adresse mail" />
                <textarea id="message" name="message" placeholder="Ecrivez votre message ici..." rows="5" cols="33"></textarea>
                <button type="button" onclick="">Envoyer</button>
            </form>
        </div>
    </div>
    <Footer></Footer>
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
            items: [],
            };
        },
        mounted() {
            axios.get("http://127.0.0.1:5000/accueil")
                .then(response => {
                    this.items = response.data;
                })
                .catch(error => {
                    console.error("Erreur lors de la récupération des données:", error);
                });
            }
        }
        
</script>


<style>
    * {
        margin: 0;
        padding: 0;
        font-family: "Poppins", sans-serif;
    }
    .presentation-container {
        padding: 15em;
        background-image: linear-gradient(
        rgba(0, 0, 0, 0.6), 
        rgba(0, 0, 0, 0.6)
      ), url(../../public/img/bg1homepage.jpg);
        background-repeat: no-repeat;
        background-position: center;
        background-attachment: fixed;
        background-size: cover;
        h1, h2 {
            color: white;
            text-align: center;
            font-size: 40px;
        }
        h1 {
            font-weight: 800;
        }
        h2 {
            font-weight: 200;
        }
    }
    .selection-container {
        background-color: #FFEDE1;
    }
    .selection {
        max-width: 1280px;
        padding-bottom: 50px;
        display: flex;
        flex-wrap: wrap;
        margin: auto;
        justify-content: space-around;
        h2 {
            width: 100%;
            font-size: 45px;
            color: #39487E;
            padding: 1em;
        }
        div{
            width: 30%;
            text-align: center;
            margin-bottom: 30px;
            img {
                background-color: #819ECC;
                border-radius: 10px;
                width: 60%;
                box-shadow: 1px 5px 20px black;
            }
        }
        a {
            width: 20%;
            text-align: center;
            text-decoration: none;
            padding: .7em 0;
            border-radius: 30px;
            background-color: #39487E;
            color: white;
            border: 2px solid #39487E;
            margin: auto;
            transition-duration: .3s;
        }
        a:hover {
            color: #39487E;
            background-color: white;
        }
    }

    .moreinfos-container {
        background-color: #39487E;
        .moreinfos{
            max-width: 1280px;
            margin: auto;
            color: white;
            background-color: #39487E;
            display: flex;
            flex-wrap: wrap;
            padding: 1.5em;
            
            h2 {
                text-align: center;
                width: 100%;
                font-size: 40px;
                padding: .5em;
            }
            .leftside {
                width: 50%;
                h3 {
                    margin-left: 30px;
                    font-size: 30px;
                    font-style: italic;
                    font-weight: 200;
                }
                p {
                    margin-top: 10px;
                    margin-left: 55px;
                    font-size: 24px;
                    font-weight: 400;
                }
            }
            img {
                width: 500px;
                margin: auto;
                border-radius: 10px;
                box-shadow: 1px 5px 20px black;
            }
        }
    }
    
    .catalogue-button-container {
        background-color: #FFEDE1;
        padding-top: 50px;
        padding-bottom: 50px;
        .catalogue-button {
            max-width: 1100px;
            padding: 2.5em;
            border-radius: 50px;
            background-color: #819ECC;
            display: flex;
            flex-wrap: wrap;
            margin: auto;
            justify-content: center;
            h2 {
                color: white;
                font-size: 35px;
                font-weight: 500;
                margin-right: 20px;
            }
            a {
                border-radius: 40px;
                text-decoration: none;
                border: 2px solid #39487E;
                padding: 1em;
                background-color: white;
                color: #39487E;
                font-weight: 600;
                transition-duration: 0.5s;
                font-size: 16px;
            }
            a:hover {
                background-color: #39487E;
                color: white;
            }
        }
    }

    .contact-form-container {
        padding: 2em;
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        background-color: #39487E;
        color: white;
        h2{
            text-align: center;
            font-size: 30px;
            width: 100%;
        }
        .contact-infos{
            max-width: 600px;
            width: 50%;
            display: flex;
            flex-wrap: wrap;
            margin: auto 0;
            h3{
                width: 70%;
                font-size: 25px;
                font-weight: 600;
                margin-left: 100px;
                margin-bottom: 15px;
            }
            h4 {
                margin-bottom: 15px;
                padding: 0.2em;
                width: 60%;
                font-weight: 300;
                margin-left: 100px;
                font-size: 15px;
            }
        }
        .separator{
            width: 0.3%;
            font-size: 1px;
            background-color: white;

        }
        .contact-form{
            max-width: 600px;
            width: 45%;
            display: flex;
            flex-wrap: wrap;
            input, textarea {
                width: 80%;
                margin: 1em;
                padding: .5em;
                border-radius: 10px;
                border: 3px solid #819ECC;
            }
            button {
                width: 30%;
                margin: 1em;
                padding: .5em;
                border-radius: 30px;
                border: 3px solid #819ECC;
                background-color: white;
                color: #819ECC;
                transition-duration: .3s;
            }
            button:hover {
                color: white;
                background-color: #819ECC;
            }
        }
    }

</style>