const express = require('express')
const app = express()
const port = 3000

let productos = [
  { id: 1, nombre: 'zapatillas', precio: 20 },
  { id: 2, nombre: 'notebook', precio: 2000 },
  { id: 3, nombre: 'lapicera', precio: 5 },
]

app.use(express.json())

// GET todos los productos
app.get('/productos', (req, res) => res.json(productos))

// GET un producto por id
app.get('/productos/:id', (req, res) => {
  const producto = productos.find(p => p.id === parseInt(req.params.id))
  if (!producto) return res.status(404).json({ message: 'Producto no encontrado' })
  res.json(producto)
})

// POST crear producto — Body JSON: { "nombre": "auriculares", "precio": 50 }
app.post('/productos', (req, res) => {
  const nuevo = { ...req.body, id: productos.at(-1).id + 1 }
  productos.push(nuevo)
  res.json(nuevo)
})

// PUT actualizar producto — Body JSON: { "precio": 99 }
app.put('/productos/:id', (req, res) => {
  const index = productos.findIndex(p => p.id === parseInt(req.params.id))
  if (index === -1) return res.status(404).json({ message: 'Producto no encontrado' })
  productos[index] = { ...productos[index], ...req.body }
  res.json({ message: 'Producto actualizado', producto: productos[index] })
})

// DELETE eliminar producto
app.delete('/productos/:id', (req, res) => {
  const existe = productos.find(p => p.id === parseInt(req.params.id))
  if (!existe) return res.status(404).json({ message: 'Producto no encontrado' })
  productos = productos.filter(p => p.id !== parseInt(req.params.id))
  res.sendStatus(204)
})

app.listen(port, () => console.log('Servidor en http://localhost:3000'))