const fs = require('./db');

class ComprasModel{
    constructor(){
        this.collection = 'compras'
        this.db = fs
    }

    async getAll() {
        const compras = this.db.collection(this.collection);
        const data = await compras.get();
        const comprasData = []
        data.forEach(doc=>{
            console.log(doc.data());
            comprasData.push(doc.data())
        })
        return comprasData;
    }

}

module.exports = ComprasModel
