require('dotenv').config()

const config = {
    port: process.env.PORT,
    dbUrl: process.env.DATABASEURL
}

module.exports = {config}