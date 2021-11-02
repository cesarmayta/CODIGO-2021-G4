const express = require('express');
const {dataAlumnos} = require('../data/alumnos');
const mysqlConnection = require('../lib/mysql');

function alumnosApi(app){
    const router = express.Router();
    app.use("/alumnos",router);

    router.get("/",async function(req,res,next){
        try{
            mysqlConnection.query('select * from alumnos',(err,rows,fields)=>{
                if(!err){
                    res.json(rows);
                }else{
                    console.log(err);
                }
            });
        }catch(err){
            next(err);
        }
    })

    router.get("/:id",(req,res)=> {
        const {id} = req.params;
        mysqlConnection.query('select * from alumnos where id = ?',[id],(err,rows,fields)=>{
            if(!err){
                res.json(rows[0]);
            }else{
                console.log(err);
            }
        });
    });

    router.post('/',(req,res)=>{
        const {nombre,email,pais} = req.body;
        console.log(nombre,email,pais);
        mysqlConnection.query('insert into alumnos(nombre,email,pais) values(?,?,?)',
        [nombre,email,pais],(err,rows,fields)=>{
            if(!err){
                res.json({status:'ok'});
            }else{
                console.log(err);
            }
        })
    });

    router.put('/:id',(req,res)=> {
        const {nombre,email,pais} = req.body;
        const {id} = req.params;
        mysqlConnection.query('update alumnos set nombre=?,email=?,pais=? where id =?',
        [nombre,email,pais,id],(err,rows,fields)=>{
            if(!err){
                res.json({status: 'Actuazación exitosa'});
            }else{
                console.log(err);
            }
        });

    });

    router.delete('/:id',(req,res)=>{
        const {id} = req.params;
        mysqlConnection.query('delete from alumnos where id = ?',[id],(err,rows,fields)=>{
            if(!err){
                res.json({status:'eliminación exitosa'});
            } else {
                console.log(err);
            }
        });
    });
}
module.exports = alumnosApi;