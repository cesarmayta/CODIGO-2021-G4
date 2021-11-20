const express = require('express')
const app = express()

const {config} = require('../config/index')
const peliculasApi = require('../routes/peliculas')

app.use(express.json())

peliculasApi(app);

//levantamos el microservicio
app.listen(config.port1,function(){
    console.log(`microservicio 1 : http://localhost:${config.port1}`)
})