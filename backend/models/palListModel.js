const mongoose = require('mongoose');


const palListSchema = new mongoose.Schema({
    key: String,
    name: String,
    price: Number,
    image: String
});