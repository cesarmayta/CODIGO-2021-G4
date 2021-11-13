//npm install express mongodb nodemon
const express = require('express');
const app = express();

const {MongoClient} = require('mongodb');

const url =  'mongodb://127.0.0.1:27017'
const client = new MongoClient(url);

const dbName = 'codigog4'

app.use(express.json());

app.get('/',(req,res)=>
    res.json({'mensaje':'api express con mongodb'})
)

app.get('/alumnos',
async (req,res)=>{
    await client.connect();
    console.log("estas conectado a la bd");
    const db = client.db(dbName);
    col = db.collection('alumnos');
    const findResult = await col.find().toArray();
    res.json(findResult)
})

app.post('/alumnos',
async (req,res)=>{
    const alumno = req.body;
    await client.connect();
    console.log("estas conectado a la bd");
    const db = client.db(dbName);
    col = db.collection('alumnos');
    const insertResult = 
    await col.insertOne({nombre:alumno.nombre,email:alumno.email,dni:alumno.dni,edad:alumno.edad});
    res.json({mensaje:'alumno registrado'})
})

app.listen(5000,()=> console.log("servidor en http://localhost:5000"));