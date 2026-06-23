const express = require('express')
const app = express()
const port = 3000

// Este middleware se ejecuta ANTES de cualquier ruta
app.use((req, res, next) => {
  console.log(`Método: ${req.method} - URL: ${req.url}`)
  next() // sin esto, el servidor nunca respondería
})

app.get('/perfil', (req, res) => res.send('Página de perfil'))
app.get('/info', (req, res) => res.send('Página de información'))

app.listen(port, () => console.log('Servidor en http://localhost:3000'))