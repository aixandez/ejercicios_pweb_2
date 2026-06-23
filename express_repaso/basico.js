const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Bienvenido')
})

app.get('/perfil', (req, res) => {
  res.send('Perfil de usuario')
})

app.listen(port, () => console.log('Servidor en http://localhost:3000'))