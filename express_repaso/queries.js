const express = require('express')
const app = express()
const port = 3000

// http://localhost:3000/suma/mac123?x=2&y=3
app.get('/suma/:computadora', (req, res) => {
  const { x, y } = req.query
  res.send(`Resultado para ${req.params.computadora}: ${parseInt(x) + parseInt(y)}`)
})

// http://localhost:3000/buscar?q=libros
app.get('/buscar', (req, res) => {
  if (req.query.q === 'libros') res.send('Lista de libros de javascript')
  else res.send('Página normal')
})

app.listen(port, () => console.log('Servidor en http://localhost:3000'))