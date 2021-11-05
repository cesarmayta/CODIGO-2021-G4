const express = require('express');
const router = express.Router();

const mysqlConnection = require('../lib/mysql');

router.get('/categoria',(req,res) => {
    mysqlConnection.query('call obtenerCategorias',(err,rows,fields) => {
        if(!err){
            res.json(rows[0]);
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

router.get('/categoria/:id/plato',(req,res)=>{
    const {id} = req.params;
    mysqlConnection.query('CALL obtenerPlatosPorCategoriaId(?)',[id],(err,rows)=>{
        if(!err){
            //https://res.cloudinary.com/dd9ad40qm/
            res.json(rows[0]);
        }else{
            console.log(err);
        }
    })
})

module.exports = router;