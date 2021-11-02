const express = require('express');
const { config } = require('./config/index');
const app = express();

app.get('/',(req,res)=> {
    res.json({mensaje:'bienvenido a mi API punto de venta'})
})

app.listen(config.port,function(){
    console.log(`SERVIDOR http://localhost:${config.port}`);
})