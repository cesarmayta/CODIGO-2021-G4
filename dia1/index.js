const express = require('express')
const app = express()
const port = 5000

app.set('view engine', 'ejs');

//creando conexion a base de datos
//sequelize
const Sequelize = require('sequelize');
const sequelize = new Sequelize({
    dialect:'sqlite',
    storage:'./database.sqlite'
})

sequelize.authenticate()
.then(()=>{
    console.log("conexion establecida");
})
.catch(err=>{
    console.log("error al conectarse");
})

//creación de modelo
const Experiencia = sequelize.define(
  'experiencia',
  {
      puesto:Sequelize.STRING,
      empresa:Sequelize.STRING,
      descripcion:Sequelize.STRING,
      periodo:Sequelize.STRING
  }
);

//migración y poblado de data
sequelize.sync({force:true})
.then
(
  ()=>
  {
      console.log("BD y tabla creada")
      Experiencia.bulkCreate(
          [
              {puesto:'Front Developer',empresa:'FREELANCE',descripcion:'Desarrollando proyectos en React.js',periodo:'Junio 2021 - Agosto 2021'},
              {puesto:'Backend Developer',empresa:'FREELANCE',descripcion:'Desarrollando proyectos en Python con Django,NodeJs con Express',periodo:'Setiembre 2021 - Diciembre 2021'},
          ]).then(function(){
              return Experiencia.findAll();
          }).then(function(experiencia){
              console.log(experiencia)
          })
  }
)


app.get('/', (req, res) => {
  Experiencia.findAll()
  .then((exp)=>{
    console.log(exp)
    res.render('index',{
      experiencias:exp,
      tituloexp:'EXPERIENCIA LABORAL'
    })
  })
  
})


app.use(express.static('static'))

app.listen(port, () => {
  console.log(`servidor en  http://localhost:${port}`)
})