const express = require('express');
const mongoose = require('mongoose');
const app = express();
const port = 5000;

mongoose.connect('mongodb+srv://Beuhnnyto:obcMfdkwnb4FVLph@beuhnnyto.tvogdgo.mongodb.net/?retryWrites=true&w=majority&appName=Beuhnnyto')
    .then(() => console.log('Connected to MongoDB...'))
    .catch(err => console.error('Could not connect to MongoDB...'));

    