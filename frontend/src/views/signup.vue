<template>
    <Header></Header>
    <div class="loginpage-container">
        <div class="loginpage">
            <div class="login-form">
                <h1>Se connecter</h1>
                <form @submit.prevent="login">
                    <p>Adresse mail</p>
                    <input type="email" id="email" v-model="loginData.email" required/><br>
                    <p>Mot de passe</p>
                    <input id="password" type="password" v-model="loginData.password" required/><br>
                    <button type="submit">Se connecter</button>
                    <p id="verifError" v-if="loginError" class="error-message">{{ loginError }}</p>
                </form>
            </div>
            <div class="separator"></div>
            <div class="signup-form">
                <h1>S'inscrire</h1>
                <form @submit.prevent="signup">
                    <p>Adresse mail</p>
                    <input type="email" id="signupEmail" v-model="signupData.email" pattern="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$" required title="Veuillez entrer une adresse e-mail valide"/><br>
                    <p>Mot de passe</p>
                    <input id="signupPassword" type="password" v-model="signupData.password" pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%?&])[A-Za-z\d@$!%?&]{8,}$" required title="Le mot de passe doit contenir au moins 8 caractères avec au moins une lettre majuscule, une lettre minuscule, un chiffre et un caractère spécial @$!%?&"/><br>
                    <button type="submit">S'inscrire</button>
                    <p id="verifError" v-if="signupError" class="error-message">{{ signupError }}</p>
                </form>
                
            </div>
        </div>
    </div>
    <Footer></Footer>
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
            loginData: {
                email: '',
                password: ''
            },
            loginError: '',
            signupData: {
                email: '',
                password: ''
            },
            signupError: ''
            };
        },
        methods: {
            login() {
                axios.post('https://palshopprojetvue.onrender.com/login', this.loginData)
                    .then(response => {
                    console.log('Login successful', response.data);
                    localStorage.setItem('loggedIn', true);
                    this.$router.push('/');
                    })
                    .catch(error => {
                    console.error('Erreur lors de la connexion', error);
                    if (error.response.status === 404) {
                        this.loginError = 'Utilisateur non trouvé.';
                    } else if (error.response.status === 400) {
                        this.loginError = 'Email ou mot de passe incorrect.';
                    } else {
                        this.loginError = 'Une erreur s\'est produite.';
                    }
                    });
            },
            signup() {
                axios.post('https://palshopprojetvue.onrender.com/register', this.signupData)
                    .then(response => {
                    console.log('Signup successful', response.data);
                    this.signupError = 'Inscription réussie';
                    })
                    .catch(error => {
                    console.error('Erreur lors de l\'inscription', error);
                    if (error.response.status === 400) {
                        this.signupError = 'L\'utilisateur existe déjà.';
                    } else {
                        this.signupError = 'Une erreur s\'est produite.';
                    }
                    });
            }
        }
    }
</script>

<style>
    *{
        margin: 0;
        padding: 0;
        font-family: "Poppins", sans-serif;
        background-color: #FFEDE1;
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
            form {
                width: 100%;
            }
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
                    font-weight: 500;
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
                    background-color: white;
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
                #verifError{
                    padding-top: 10px;
                    margin: auto;
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

        @media screen and (max-width: 1279px) {
            .loginpage {
                .login-form, .signup-form {
                    width: 100%;
                }
                .separator {
                    display: none;
                }
            }
            
        }
    }
    
</style>