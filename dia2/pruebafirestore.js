var admin = require("firebase-admin");

var serviceAccount = require('./codigog4-12d8d-firebase-adminsdk-8ybhq-f00243b3fa.json');

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://codigog4-12d8d-default-rtdb.firebaseio.com"
});

console.log("estas conectado a firestore");

const fs = admin.firestore();

async function getAll(db) {
    // [START firestore_data_get_all_documents]
    const alumnos = db.collection('alumnos');
    const snapshot = await alumnos.get();
    snapshot.forEach(doc => {
      console.log(doc.id, '=>', doc.data());
    });
    // [END firestore_data_get_all_documents]
  }
getAll(fs);

/*
const db = admin.database();
const ref = db.ref("codigo/g4");

const alumnoRef = ref.child("alumnos");

alumnoRef.set({
    alumnos:{
        nombre:"carlos pacheco",
        email:"carlos@gmail.com"
    }
})

console.log("Alumno creado")
*/
