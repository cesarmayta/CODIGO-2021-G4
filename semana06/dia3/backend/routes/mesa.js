const express = require('express');
const router = express.Router();

const mysqlConnection = require('../lib/mysql');

router.get('/mesa',(req,res) => {
    mysqlConnection.query('select * from tbl_mesa',(err,rows,fields) => {
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