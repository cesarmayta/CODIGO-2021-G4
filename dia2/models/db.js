var admin = require("firebase-admin");
const {config} = require('../config/index')

const DBURL = config.dbUrl;

var serviceAccount = require('../tokenfirebase.json');

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: DBURL
});

const fs = admin.firestore();

module.exports = fs;