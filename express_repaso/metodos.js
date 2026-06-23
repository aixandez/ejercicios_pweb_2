const express = require('express')
const app = express()
const port = 3000

app.get('/productos', (req, res) => res.send('Lista de productos'))
app.post('/producto', (req, res) => res.send('Creando producto'))
app.put('/producto', (req, res) => res.send('Actualizando producto'))
app.delete('/producto', (req, res) => res.send('Eliminando producto'))

// Responde a CUALQUIER método HTTP
app.all('/info', (req, res) => res.send('Información del servidor'))

app.listen(port, () => console.log('Servidor en http://localhost:3000'))