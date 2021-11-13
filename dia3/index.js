const express = require('express');
const app = express();

app.use(express.json());



const port = 5000;
app.listen(port,()=> console.log(`http://localhost:${port}`));

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
const Alumnos = sequelize.define(
    'alumnos',
    {
        nombre:Sequelize.STRING,
        email:Sequelize.STRING
    }
);

//migración y poblado de data
sequelize.sync({force:true})
.then
(
    ()=>
    {
        console.log("BD y tabla creada")
        Alumnos.bulkCreate(
            [
                {nombre:'cesar mayta',email:'cesarmayta@gmail.com'},
                {nombre:'Luisa Lane',email:'luisa@dailyplanet.com'},
                {nombre:'Ana Scott',email:'anita@scotts.com'}
            ]).then(function(){
                return Alumnos.findAll();
            }).then(function(alumnos){
                console.log(alumnos)
            })
    }
)

app.get('/',(req,res)=>{
    res.send("Bienvenido a mi app")
})

app.get('/alumnos',(req,res)=>{
    Alumnos.findAll()
    .then(
        alumnos => res.json(alumnos)
    )
})

app.get('/alumnos/:id',(req,res)=>{
    Alumnos.findAll({where: {id:req.params.id}})
    .then(
        alumnos => res.json(alumnos)
    );
})

app.post('/alumnos',(req,res)=>{
    Alumnos.create(
        {
            nombre: req.body.nombre,
            email: req.body.email
        }
    ).then(function(alumnos){
        res.json(alumnos);
    })
})

app.put('/alumnos/:id',(req,res)=>{
    Alumnos.findByPk(req.params.id)
    .then(function(alumnos){
        alumnos.update(
            {
                nombre:req.body.nombre,
                email:req.body.email
            }
        ).then(function(alumnos){
            res.json(alumnos);
        })
    })
})

app.delete('/alumnos/:id',(req,res)=>{
    Alumnos.findByPk(req.params.id)
    .then(function(alumnos){
        alumnos.destroy();
    }).then(function(alumnos){
        res.sendStatus(200);
    })
})

