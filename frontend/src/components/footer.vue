<template>
    <footer>
    <div class="footer-container">
        <h1>PALSHOP</h1>
        <div class="separator">.</div>
        <h2>Cliquez, Achetez, Dominez</h2>
        <div class="informations-container">
            <div class="about-us">
                <h3>A propos</h3>
                <ul>
                    <a href='/'>Accueil</a><br>
                    <a href='/Catalogue'>Catalogue</a><br>
                    <a href='/login'>S'inscrire/Se connecter</a><br>
                    <a href='/'>CGU/CGV</a>
                </ul>
            </div>
            <div class="social-media">
                <h3>Nos Réseaux</h3>
                <ul>
                    <a href='https://www.linkedin.com'>Linkedin</a><br>
                    <a href='https://www.instagram.com'>Instagram</a><br>
                    <a href='https://www.twitter.com'>Twitter</a><br>
                    <a href='https://www.facebook.com'>Facebook</a>
                </ul>
            </div>
            <div class="contact">
                <h3>Contact</h3>
                <ul>
                    <h4>PALSHOP</h4>
                    <h4>01.XX.XX.XX.XX</h4>
                    <h4>contact@palshop.fr</h4>
                </ul>
            </div>
        </div>
        <p>© Copyright, tous droits réservés. Site réalisé par LSA.</p>
    </div>
    </footer> 
    
</template>

<style>
    * {
        margin: 0;
        padding: 0;
        font-family: "Poppins", sans-serif;

    }
    footer {
        display: flex;
        flex-wrap: wrap;
        background-color:#FFEDE1;
        .footer-container{
        max-width: 1280px;
        width: 100%;
        margin: auto;
        display: flex;
        flex-wrap: wrap;
        }

        h1, h2, .separator{
            color: #39487E;
            width: 95%;
            margin-left: 2.5%;
        }
        .separator{
            background-color: #39487E;
            font-size: 2px;
            margin-bottom: 8px;
        }
        h1{
            font-weight: 900;
        }
        h2 {
            font-weight: 400;
            font-size: 20px;
        }
        .informations-container {
            display: flex;
            flex-wrap: wrap; 
            width: 40%;
            margin-left: auto;
            margin-bottom: 20px;
            .about-us, .social-media, .contact {
                width: 30%;
                color: #424040;
                font-weight: 300;
                font-size: 12px;
            }
            h3 {
                font-weight: 600;
                margin-bottom: 8px;
            }
            .about-us a, .social-media a{
                width: 100%;
                text-decoration: none;
                color: #424040;
                font-weight: 300;
            }
            h4 {
                font-weight: 300;
            }
        }
        p {
            width: 100%;
            text-align: center;
            font-size: 10px;
        }
    }
    

</style>