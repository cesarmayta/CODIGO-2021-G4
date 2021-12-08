const express = require('express');
const router = express.Router();

const mysqlConnection = require('../lib/mysql');

router.get('/pedido',(req,res) => {
    
    mysqlConnection.query(
    "SELECT DATE_FORMAT(p.pedido_fech, '%Y-%m-%d %H:%i:00') as pedido_fech,pp.pedido_plato_plato_id as plato_id,pp.pedido_plato_can as pedidoplato_cant FROM tbl_pedido_plato pp INNER JOIN tbl_pedido p on pp.pedido_plato_pedido_id = p.pedido_id",
    (err,rows,fields) => {
        if(!err){
                res.json(
                    { 
                        "ok":true,
                        "pedidos":[
                            {...rows[0],
                                PedidoPlatos:rows
                            }
                        ]

                    }
                    );
        }else{
            console.log(err);
        }
    });
});

router.post('/pedido',(req,res) => {
    const pedido = req.body;
    let pedidoId = 0;
    let status = false;
    console.log("nro :" + pedido.pedido_nro);
    console.log("fecha :" + pedido.pedido_fech);
    console.log("estado :" + pedido.pedido_est);
    console.log("mesa :" + pedido.mesa_id);
    console.log("empleado :" + pedido.usu_id);
    pedido.pedidoplatos.forEach(item => console.log(item));
    mysqlConnection.query(
        'insert into tbl_pedido(pedido_nro,pedido_fech,pedido_est,mesa_id,empleado_id) values(?,?,?,?,?)'
        ,[pedido.pedido_nro,pedido.pedido_fech,pedido.pedido_est,pedido.mesa_id,pedido.usu_id],
        (err,rPedidoId,fields) => 
        {
            if(!err){
                //consultar ultimo id
                pedidoId = rPedidoId.insertId;
                console.log(pedidoId);
                //registrar detalle
                pedido.pedidoplatos.forEach(item => {
                    console.log("registando pedido plato:"  + item); 
                        mysqlConnection.query(
                        'insert into tbl_pedido_plato(pedido_plato_can,pedido_plato_pedido_id,pedido_plato_plato_id) values(?,?,?)'
                        ,[item.pedidoplato_cant,pedidoId,item.plato_id]
                        ,(err,rows,fields) => {
                            if(!err){
                                
                            }else{
                                console.log(err);
                            }
                        });
                }  
                );
                res.json(
                    { 
                        "ok":true,
                    }
                    );
            
            }
            else{
                console.log(err);
            }
        });
});
               
module.exports = router;