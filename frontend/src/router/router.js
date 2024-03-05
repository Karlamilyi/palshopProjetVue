import Vue from 'vue'
import VueRouter from 'vue-router'
import home from '../views/home.vue'
import Panier from '../views/panier.vue'
import pal from '../views/pal.vue'
import login from '../views/login.vue'
import signup from '../views/signup.vue'
import Notfound from '../views/Notfound.vue'

Vue.use(VueRouter)

const routes =[

    {
        path:'/',
        name:'Home',
        component:home,
    },
    {
        path:'/login',
        name:'login',
        component:login,
    },
    {
        path:'/panier/:id',
        name:'panier',
        component:Panier,
    },
    {
        path:'/pal/:id',
        name:'pal',
        component:pal,
    },
    {
        path:'/signup',
        name:'singup',
        component:signup,
    },
    {
        path:'*',
        component:Notfound,
    }
]

const router = new VueRouter({
    mode:'history',
    base: process.env.BASE_URL,
    routes
})
export default router