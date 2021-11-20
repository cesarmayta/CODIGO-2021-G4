const express = require('express')
const app = express()

const {config} = require('../config/index')
const usuariosApi = require('../routes/usuarios')

app.use(express.json())

usuariosApi(app);

//levantamos el microservicio
app.listen(config.port2,function(){
    console.log(`microservicio 1 : http://localhost:${config.port2}`)
})