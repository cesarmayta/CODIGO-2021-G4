const express = require('express');
const app = express();

const db = require('./models/db')
const productoController = require('./controllers/productosController');

const port = 5000;

//app.use(express.json());

app.use('/api',productoController);
app.get('',(req,res)=>
    res.json({'mensaje':'api express con mongoose'})
)

app.listen(port,()=> console.log(`servidor en http://localhost:${port}`));