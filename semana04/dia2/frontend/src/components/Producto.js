import { Component } from "react"
import Button from './Button'

const styles = {
    producto: {
        border: 'solid 1px #eee',
        boxShadow: '0 5px 5px rgb(0,0,0,0.1)',
        width:'30%',
        padding: '10px 15px',
        borderRadius: '5px',
    },
    img: {
        width:'70%'
    }
}

class Producto extends Component {
    render() {
        console.log(this.props)
        const { producto,agregarAlCarro } = this.props
        return (
           <div style={styles.producto}>
               <img style={styles.img} alt={producto.nombre} src={producto.imagen}/>
               <h3>{producto.nombre}</h3>
               <h2>{producto.precio}</h2>
               <Button onClick={() => agregarAlCarro(producto)}>
                   Agregar al carro
               </Button>
           </div>
        )
    }
}

export default Producto