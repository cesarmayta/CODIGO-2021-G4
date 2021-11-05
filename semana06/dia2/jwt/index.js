const express = require('express');
const app = express();

const jwt = require('jsonwebtoken');

app.get('/',(req,res)=>{
    res.json({
        mensaje:'Ejemplo de jwt'
    })
})




app.post('/login',(req,res) =>{
    const usuario = {
        id:1,
        usuario:"admin",
        email:"cesarmayta@gmail.com"
    }
    jwt.sign({usuario},'secretkey',{expiresIn: '90s'},(err,token)=>{
        res.json({
            token
        })
    })
})

app.post('/publico',(req,res)=>{
    res.json({
        mensaje:'acceso publico'
    })
})

app.post('/privado',validarToken,(req,res)=>{
    jwt.verify(req.token,'secretkey',
    (err,authData)=>{
        if(err){
            res.json({
                mensaje:'token invalido',
                err
            })
        }else{
            res.json({
                mensaje:'acceso privado',
                authData
            })
        }
    })
})

function validarToken(req,res,next){
    const bearerHeader = req.headers['authorization'];
    if(typeof bearerHeader !== 'undefined'){
        const bearer = bearerHeader.split(' ')
        const bearerToken = bearer[1]
        req.token = bearerToken
        next()
    }else{
        res.sendStatus(403);
    }
}

app.listen(5000,()=> console.log('servidor corriendo en http://localhost:5000'))