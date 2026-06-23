const express = require('express')
const app = express()
const port = 3000

app.use(express.text())       // para recibir texto plano
app.use(express.json())       // para recibir JSON
app.use(express.urlencoded({ extended: false }))  // para recibir formularios

// Thunder Client -> POST -> Body -> Text: "Hola"
app.post('/texto', (req, res) => {
  res.send(`Recibí el texto: ${req.body}`)
})

// Thunder Client -> POST -> Body -> JSON: { "email": "pepe@gmail.com" }
app.post('/usuario', (req, res) => {
  console.log(req.body)
  res.send(`Usuario creado con email: ${req.body.email}`)
})

// Thunder Client -> POST -> Body -> Form: username=pepe, age=18
app.post('/usuario2', (req, res) => {
  console.log(req.body)
  res.send(`Usuario del formulario: ${req.body.username}, edad: ${req.body.age}`)
})

app.listen(port, () => console.log('Servidor en http://localhost:3000'))