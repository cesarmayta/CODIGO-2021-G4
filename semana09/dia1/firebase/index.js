
var admin = require("firebase-admin");

var serviceAccount = require("../credencialesfirebase.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://codigog4-12d8d-default-rtdb.firebaseio.com"
});

module.exports = admin;
