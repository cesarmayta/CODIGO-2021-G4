const {MongoClient} = require('mongodb');

const url =  'mongodb://127.0.0.1:27017'
const client = new MongoClient(url);

const dbName = 'codigog4'

async function main(){
    await client.connect();
    console.log("estas conectado a la bd");
    const db = client.db(dbName);
    const col = db.collection('alumnos');

    const insertResult = await col.insertOne({nombre:"juan perez",email:"juanp@yahoo.com",dni:"46464642",edad:15});
    console.log(insertResult);
    const findResult = await col.find().toArray();
    console.log(findResult);

    return 'done.';
}

main()
.then(console.log)
.catch(console.error)
.finally(()=> client.close());

