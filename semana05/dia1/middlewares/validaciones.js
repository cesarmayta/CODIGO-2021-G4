function validacionAlumno(req,res,next){
    if(req.method == 'POST'){
        if(req.body.nombre != null && req.body.email != null && req.body.pais != null){
            next();
        } else{
            res.status(400).json({
                status:'debe llenar todos los datos'
            });
        }
    }
}

module.exports = validacionAlumno