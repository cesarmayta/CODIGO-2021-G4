require('dotenv').config()

const config = {
    port1: process.env.PORT1,
    port2: process.env.PORT2,
    mongoURI: process.env.MONGOURI,
    mongoDBName: process.env.MONGODBNAME
}

module.exports = {config}