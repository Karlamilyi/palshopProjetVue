<template>
    <header>
        <div class="navbar">
            <h1>PALSHOP</h1>
            <ul>
                <a href='/catalogue'>Catalogue</a>
                <a href='/panier'>Panier</a>
                <a id="connexion" href='/login'>Connexion / Inscription</a>
            </ul>
        </div>
    </header>
</template>

<style>
    * {
        margin: 0;
        padding: 0;
        font-family: "Poppins", sans-serif;
        color: white;
    }

    .navbar {
        display: flex;
        flex-wrap: wrap;
        background-color: #39487E;
        padding: 1em;
        ul {
            margin: auto 0 auto 50px;
            display: flex;
            a {
                font-weight: 100;
                text-decoration: none;
                margin: 0 50px 0 20px;
                transition: ease-in-out;
                transition-duration: 0.3s;

            }
            #connexion {
                margin-left: 500px;
            }
            a:hover{
                transform: scale(1.05);
            }
        }
    }
</style>