const { MongoClient } = require('mongodb');

const uri = 'mongodb+srv://Beuhnnyto:obcMfdkwnb4FVLph@beuhnnyto.tvogdgo.mongodb.net/?retryWrites=true&w=majority&appName=Beuhnnyto';


// Create a new MongoClient
const client = new MongoClient(uri);

// Connect the client to the server
client.connect(err => {
  // Perform actions on the collection object
  if (err) {
    console.log('Error connecting to the database');
  } else {
    console.log('Connected to the database');
  }
  client.close();
});

