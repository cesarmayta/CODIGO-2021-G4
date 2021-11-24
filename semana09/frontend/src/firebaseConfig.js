import * as firebase from "firebase";
import "firebase/auth";
//import dataConfig from './dataConfig'

const app = firebase.initializeApp(
    {
        apiKey: "AIzaSyBTcYwk0rmlxwT4odohWoQqOgt1pF0FcQc",
        authDomain: "codigog4-12d8d.firebaseapp.com",
        databaseURL: "https://codigog4-12d8d-default-rtdb.firebaseio.com",
        projectId: "codigog4-12d8d",
        storageBucket: "codigog4-12d8d.appspot.com",
        messagingSenderId: "295138741281",
        appId: "1:295138741281:web:1123562cc3327d246f6760",
        measurementId: "G-3C7X3HZXHZ"
    }
);

/*const googleAuthProvider = new firebase.auth.GoogleAuthProvider();
const facebookAuthProvider = new firebase.auth.FacebookAuthProvider();
const githubAuthProvider = new firebase.auth.GithubAuthProvider();*/

export default app;