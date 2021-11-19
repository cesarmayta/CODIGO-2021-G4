const express = require('express')
const ComprasModel = require('../models/compras')

function comprasController(app){
    const router = express.Router();
    app.use('/compras',router);

    const cp = new ComprasModel();

    router.get('/',async function(req,res,next){
        try{
            const compras = await cp.getAll()
            res.render('compras',{
                lstCompras:compras
            })

        }catch(err){
            next(err)
        }
    })
}

module.exports = comprasController