const express = require('express');
const firebase = require("./firebase")
const app = express();

app.get("/",(req,res)=>{
    res.json({
        status:true,
        message:'bienvenido a mi api'
    })
})

app.get("/protegido",(req,res)=>{
    console.log("accediendo a ruta protegida...");
    const headerToken = req.headers.authorization;
    if(!headerToken){
        return res.status(401).json({
            status:false,
            message:"No esta acciendo con un token"
        })
    }
    if(headerToken && headerToken.split(" ")[0] !== "Bearer"){
        return res.status(401).json({
            status:false,
            message: "Token no valido"
        })
    }
    //validar token en firebase
    const token = headerToken.split(" ")[1];
    firebase.auth().verifyIdToken(token)
    .then(()=>{
        res.json({
            status:true,
            message:"tienes acceso porque esta logueado a firebase"
        })
    }).catch(()=>{
        res.status(401).json({
            status:false,
            message:"token no se reconoce en firebase"
        })
    })
})

app.listen(5000, ()=> console.log("sevidor en http://localhost:5000"))