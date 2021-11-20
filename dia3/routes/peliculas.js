const express = require('express')
const PeliculasService = require('../services/peliculas')

function peliculasApi(app){
    const router = express.Router()
    app.use('/api',router)

    const ps = new PeliculasService()

    router.get('/',async function(req,res,next){
        try {
            const peliculas = await ps.getAll()

            res.status(200).json({
                status:true,
                content:peliculas
            })
        }catch(err){
            next(err)
        }
    })

    router.post('/',async function(req,res,next){
        const {body:peliculaData} = req

        console.log("datos de pelicual routes:",peliculaData)

        try {
            const peliculaId = await ps.create({peliculaData})

            res.status(201).json({
                status:true,
                content:peliculaId
            })
        }catch(err){
            next(err)
        }
    })

    router.put('/:peliculaId',async function(req,res,next){
        const {body:peliculaData} = req
        const {peliculaId} = req.params

        console.log("id de pelicula:",peliculaId)

        console.log("datos de pelicula routes:",peliculaData)

        try {
            const peliculaActualizarId = await ps.update({peliculaId,peliculaData})

            res.status(201).json({
                status:true,
                content:peliculaActualizarId
            })
        }catch(err){
            next(err)
        }
    })

    router.delete('/:peliculaId',async function(req,res,next){

        const {peliculaId} = req.params

        console.log("id de pelicula:",peliculaId)

        try {
            const peliculaEliminarId = await ps.delete({peliculaId})

            res.status(200).json({
                status:true,
                content:peliculaEliminarId
            })
        }catch(err){
            next(err)
        }
    })


}



module.exports = peliculasApi