const http = require('http');

http.createServer(function(req,res){
    console.log("servidor encendido");
    res.write('<h1>HOLA MUNDO NODEJS</h1>');
    res.end();
}).listen(4000);

