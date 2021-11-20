const express = require('express')

function usuariosApi(app){
    const router = express.Router();
    app.use('/api',router);

    router.get('/',function(req,res){
        res.status(200).json({
            status:true,
            content:'usuarios'
        })
    })
}

module.exports = usuariosApi