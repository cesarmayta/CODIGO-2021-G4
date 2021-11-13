const express = require('express');
const Productos = require('../models/productos');
const router = express.Router();
router.use(express.json());

router.route('/productos')
.post(function(req,res){
    console.log(req.body);
    const productos = new Productos();
    const productoData = req.body;
    productos.nombre = productoData.nombre;
    productos.precio = productoData.precio;
    productos.save(function (error){
        if(error){
            res.status(500).send("error en el registro : " + error);
        }
        else{
            res.json({'mensaje':'producto registrado'})
        }
    })
})
.get(function(req,res){
    Productos.find(function(error,productos){
        if(error){
            res.status(500).send("error : " + error);
        }
        else{
            res.json(productos);
        }
    })
})

module.exports = router