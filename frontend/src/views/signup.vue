<template>
    <Header></Header>
    <div class="loginpage-container">
        <div class="loginpage">
            <div class="login-form">
                <h1>Se connecter</h1>
                <p>Adresse mail</p>
                <input type="email" id="email" required/><br>
                <p>Mot de passe</p>
                <input id="password" name="password" required/><br>
                <button type="button" onclick="">Se connecter</button>
            </div>
            <div class="separator"></div>
            <div class="signup-form">
                <h1>S'inscrire</h1>
                <p>Adresse mail</p>
                <input type="email" id="email" required/><br>
                <p>Mot de passe</p>
                <input id="password" name="password" required/><br>
                <button type="button" onclick="">S'inscrire</button>
            </div>
        </div>

        
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
        }
    }
</script>

<style>
    *{
        margin: 0;
        padding: 0;
        font-family: "Poppins", sans-serif;

    }
    .loginpage-container {
        background-color: #FFEDE1;
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        .loginpage {
            max-width: 1280px;
            width: 100%;
            display: flex;
            flex-wrap: wrap;
            color: #39487E;
            .login-form, .signup-form {
                justify-content: center;
                padding: 5em 0;
                width: 49%;
                display: flex;
                flex-wrap: wrap;
                text-align: center;
                h1{
                    width: 100%;
    
                    text-align: center;
                }
                p {
                    width: 50%;
                    font-weight: 700;
                    font-size: 20px;
                    margin: 30px 0 0 0;
                }
                input {
                    width: 60%;
                    padding: 1em 0;
                    margin: 1em;
                    border: 3px solid #39487E;
                    border-radius: 10px;
                    font-size: 15px;
                }
                button {
                    margin-top: 20px;
                    width: 40%;
                    padding: .7em 0;
                    font-size: 15px;
                    border: 3px solid #39487E;
                    border-radius: 10px;
                    background-color: white;
                    color: #39487E;
                    font-weight: 600;
                    transition-duration: .3s;
                }
    
                button:hover{
                    color: white;
                    background-color: #39487E;
                }
            }
            .separator {
                width: .3%;
                background-color: #39487E;
                margin-top: 50px;
            }
            .signup-form {
                width: 45%;
            }
        }
    }
    
</style>