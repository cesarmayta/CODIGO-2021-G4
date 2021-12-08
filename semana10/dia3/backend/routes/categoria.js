const express = require('express');
const router = express.Router();

const mysqlConnection = require('../lib/mysql');

router.get('/categoria',(req,res) => {
    mysqlConnection.query('call obtenerCategorias',(err,rows,fields) => {
        if(!err){
            res.json(
                { 
                    "ok":true,
                    "content": rows[0]
                }
                );
        }else{
            console.log(err);
        }
    });
});

router.get('/categoria/:id',(req,res) => {
    const {id} = req.params;
    mysqlConnection.query('CALL obtenerCategoriaPorId(?)',[id],(err,rows,fields)=>
    {
        if(!err){
            res.json(rows[0]);
        }else{
            console.log(err);
        }
    });
});

router.get('/categoria/:id/platos',(req,res)=>{
    const {id} = req.params;

    mysqlConnection.query('CALL obtenerCategoriaPorId(?)',[id],(err,rows)=>{
        let rCategoria = {};
        let rPlatos = []

        if(!err){
            //https://res.cloudinary.com/dd9ad40qm/
            rCategoria = rows[0];

            mysqlConnection.query('CALL obtenerPlatosPorCategoriaId(?)',[id],(err,rows)=>{
                if(!err){
                    //https://res.cloudinary.com/dd9ad40qm/
                    rPlatos = rows[0];
                }else{
                    console.log(err);
                }

                return res.json({
                    "ok": true,
                    "content": {
                        ...rCategoria[0],
                        "Platos": rPlatos
                    }
                })
            })
        }else{
            console.log(err);
        }
    })
})

module.exports = router;