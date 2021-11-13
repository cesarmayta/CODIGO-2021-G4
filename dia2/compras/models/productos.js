const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const ProductoSchema = new Schema({
    nombre:String,
    precio:Number
});

module.exports = mongoose.model('productos',ProductoSchema);