import { Component } from 'react'
import Productos from './components/Productos'
import Layout from './components/Layout'
import Navbar from './components/Navbar'
import Title from './components/Title'
import axios from 'axios'

class App extends Component {
  state = {
    productos : [
      //{nombre: 'Samsung Galaxy A20S',precio:900,imagen:'https://res.cloudinary.com/dd9ad40qm/image/upload/v1629321307/bjaqxmhi4k5qj9hopzji.jpg'},
      //{nombre: 'LAPTOP HP 5000',precio:3500,imagen:'https://res.cloudinary.com/dd9ad40qm/image/upload/v1629326341/yj9qdcywfvtx92pbblor.webp'},
      //{nombre: 'PC GAMER TEROS',precio:2000,imagen:'https://res.cloudinary.com/dd9ad40qm/image/upload/v1629317263/dyefuxgv6vfndr5jauok.jpg'},
    ],
    carro : [
      //{name: 'Samsung Galaxy A20S',price:900,img:'https://res.cloudinary.com/dd9ad40qm/image/upload/v1629321307/bjaqxmhi4k5qj9hopzji.jpg', cantidad: 1},
    ],
    esCarroVisible: false
  }

  componentDidMount(){
    axios.get('http://127.0.0.1:8000/productos')
    .then(res=> {
      console.log(res.data)
      this.setState({productos : res.data})
    })
  }


  agregarAlCarro = (producto) => {
    const { carro } = this.state
    if(carro.find(x => x.nombre === producto.nombre)) {
      const newCarro = carro.map(x => x.nombre === producto.nombre
        ? ({
          ...x,
          cantidad: x.cantidad + 1
        })
        : x)
      return this.setState({carro: newCarro})
    }
    return this.setState({
      carro: this.state.carro.concat({
        ...producto,
        cantidad: 1,
      })
    })
  }

  mostrarCarro = () => {
    if(!this.state.carro.length){
      return
    }
    this.setState({esCarroVisible: !this.state.esCarroVisible})
  }

  render(){
    const {esCarroVisible} = this.state
    return (
      <div>
        <Navbar carro={this.state.carro} 
        esCarroVisible={esCarroVisible} 
        mostrarCarro={this.mostrarCarro}/>
        <Layout>
          <Title/>
          <Productos
            agregarAlCarro={this.agregarAlCarro}
            productos={this.state.productos}
          />
        </Layout>
      </div>
    )
  }
}



export default App;
