const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => res.send('Bienvenido'))
app.get('/perfil', (req, res) => res.send('Perfil de usuario'))
app.get('/clima', (req, res) => res.send('El clima actual es lluvioso'))

// Si ninguna ruta coincide, devuelve 404
app.use((req, res) => {
  res.status(404).send('La página no existe')
})

app.listen(port, () => console.log('Servidor en http://localhost:3000'))