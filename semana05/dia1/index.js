const express = require('express')
const {config} = require('./config/index');
const alumnosApi = require('./routes/alumnos.js');

const app = express()

app.get('/',(req,res)=> {
    res.json({mensaje:'bienvenido a mi api'})
})

alumnosApi(app)

app.listen(config.port,() =>{
    console.log(`Servidor en http://localhost:${config.port}`)
})

