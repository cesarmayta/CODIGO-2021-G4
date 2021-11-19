const express = require('express')
const {config} = require('./config/index')

const comprasController = require('./controllers/compras')

const app = express()
const port = config.port;

app.set('view engine','ejs');

comprasController(app);

app.listen(port,() => {
    console.log(`servidor corriendo en http://localhost:${port}`)
})