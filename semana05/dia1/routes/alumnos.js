const express = require('express');
const {dataAlumnos} = require('../data/alumnos');

function alumnosApi(app){
    const router = express.Router();
    app.use("/alumnos",router);

    router.get("/",async function(req,res,next){
        try{
            const alumnos = await Promise.resolve(dataAlumnos);

            res.status(200).json({
                status:'OK',
                data: alumnos
            })
        }catch(err){
            next(err);
        }
    })
}
module.exports = alumnosApi;