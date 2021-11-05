const express = require('express');
const { config } = require('./config/index');
const app = express();

app.use(express.json());

app.get('/',(req,res)=> {
    res.json({mensaje:'bienvenido a mi API punto de venta'})
})

app.use(require('./routes/categoria'));
app.use(require('./routes/empleado'));

app.listen(config.port,function(){
    console.log(`SERVIDOR http://localhost:${config.port}`);
})