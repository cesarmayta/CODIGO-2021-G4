const express = require('express')
const {config} = require('./config/index');
const alumnosApi = require('./routes/alumnos.js');
const validacionAlumno = require('./middlewares/validaciones');

const app = express()
app.use(express.json());
app.use(validacionAlumno);

app.get('/',(req,res)=> {
    res.json({mensaje:'bienvenido a mi API alumnos'})
})

alumnosApi(app)

app.listen(config.port,() =>{
    console.log(`Servidor en http://localhost:${config.port}`)
})

