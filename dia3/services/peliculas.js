const MongoLib = require('../lib/mongo')

class peliculasService{
    constructor(){
        this.collection = 'peliculas'
        this.mongoDB = new MongoLib();
    }

    async getAll(){
        const data = await this.mongoDB.getAll(this.collection)
        return data || []
    }

    async create({peliculaData}){
        console.log("datos de pelicula service:",peliculaData)
        const peliculaId = await this.mongoDB.create(this.collection,peliculaData)
        return peliculaId || 0;
    }

    async update({peliculaId,peliculaData}){
        const updatePeliculaId = await this.mongoDB.update(
            this.collection,
            peliculaId,
            peliculaData
        )
        return updatePeliculaId;
    }

    async delete({peliculaId}){
        const deletePeliculaId = await this.mongoDB.delete(
            this.collection,peliculaId
        )
        return deletePeliculaId;
    }

}

module.exports = peliculasService