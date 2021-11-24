import React, { useEffect, useContext ,useState} from "react";
import Header from "../components/Header";
import { Layout } from "antd";
import { Auth } from "../context/AuthContext";
import { withRouter } from "react-router";

const Dashboard=({history}) =>{
    const { Content, Footer } = Layout;
    const { usuario } = useContext(Auth);
    const [nombre, setnombre,mensaje,setmensaje] = useState(null)

    useEffect(() => {
        
        if (usuario===null) {
            history.push("/login");
        }
        usuario?usuario.displayName?setnombre(usuario.displayName):setnombre(usuario.email):setnombre(null)

        async function cargarProtegido(){
            const request = await fetch('http://localhost:5000/protegido',{
                headers : {
                    Authorization: "Bearer " + localStorage.getItem("@token")
                }
            })
            const mensajeBack = await request.json();
            console.log(mensajeBack)
        }
    }, [history, usuario]);

    
        return (
            <Layout style={{ height: "100vh" }}>
                <Header
                    titulo="Firebase Auth"
                    subtitulo="Login con Firebase y ReactJS"
                />
                <Content style={{ padding: "0 50px", marginTop: 40 }}>
                    <div
                        style={{
                            background: "#fff",
                            padding: 24,
                            minHeight: "80vh"
                        }}
                    >
                        Hola {nombre} :)
                        
                    </div>
                </Content>
                <Footer style={{ textAlign: "center" }}>
                    Creado por Nicolás Morales
                </Footer>
            </Layout>
        );
    
}
export default withRouter(Dashboard);
