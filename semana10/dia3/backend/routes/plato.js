const express = require('express');
const router = express.Router();

const mysqlConnection = require('../lib/mysql');

router.get('/plato',(req,res) => {
    mysqlConnection.query('select * from tbl_plato',(err,rows,fields) => {
        if(!err){
            res.json(
                { 
                    "ok":true,
                    "content": rows
                }
                );
        }else{
            console.log(err);
        }
    });
});


module.exports = router;