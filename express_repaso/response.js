const express = require('express')
const app = express()
const port = 3000

// Responde texto
app.get('/', (req, res) => res.send('Bienvenido'))

// Responde JSON
app.get('/usuario', (req, res) => res.json({ nombre: 'pepe' }))

// Responde solo un código de estado (sin contenido)
app.get('/isAlive', (req, res) => res.sendStatus(204))

app.listen(port, () => console.log('Servidor en http://localhost:3000'))