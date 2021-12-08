const express = require('express');
const { config } = require('./config/index');
const cors = require('cors')


const app = express();

app.use(cors());

app.use(express.json());

app.get('/',(req,res)=> {
    res.json({mensaje:'bienvenido a mi API punto de venta'})
})

app.use(require('./routes/categoria'));
app.use(require('./routes/empleado'));
app.use(require('./routes/mesa'));
app.use(require('./routes/pedido'));
app.use(require('./routes/plato'));

app.listen(config.port,function(){
    console.log(`SERVIDOR http://localhost:${config.port}`);
})