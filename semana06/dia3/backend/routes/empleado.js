const express = require('express');
const router = express.Router();
const jwt = require('jsonwebtoken');

const mysqlConnection = require('../lib/mysql');

router.get('/empleado/:usuario_id',(req,res) => {
    const {usuario_id} = req.params;
    mysqlConnection.query('select * from tbl_empleado where usuario_id = ?',[usuario_id],(err,rows,fields) =>
     {
        if(!err){
            res.json(rows[0]);
        }else{
            console.log(err);
        }
    });
});

router.get('/auth/empleado',validarToken,(req,res)=>{
    jwt.verify(req.token,'django-insecure-w%r)w-16cr%of&ms&c@lbc-44o$w_^oo+%@__fmo1-)3k)$hle',
    (err,authData)=>{
        if(err){
            res.json({
                mensaje:'acceso denegado',
                err
            })
        }else{
            const usuario_id = authData.user_id
            console.log(authData.user_id);
            mysqlConnection.query('select * from tbl_empleado where usuario_id = ?',[usuario_id],(err,rows,fields) =>
            {
               if(!err){
                   res.json(
                       {ok:true,
                        content:rows[0]
                       });
               }else{
                   console.log(err);
               }
           });
        }
    })
})

function validarToken(req,res,next){
    const bearerHeader = req.headers['authorization'];
    console.log("token:",bearerHeader);
    if(typeof bearerHeader !== 'undefined'){
        const bearer = bearerHeader.split(' ')
        const bearerToken = bearer[1]
        console.log(bearerToken)
        req.token = bearerToken
        next()
    }else{
        console.log("error al conectarse al endpoint");
        res.sendStatus(403);
    }
}

module.exports = router;