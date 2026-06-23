const http = require('http')

const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html' })
  res.end('<h1>Servidor Activo - Programación Web 2</h1>')
})

server.listen(3000, () => {
  console.log('Servidor funcionando en http://localhost:3000')
})

server.on('error', (e) => {
  if (e.code === 'EADDRINUSE') {
    console.log('Error: El puerto 3000 ya está en uso')
  } else {
    console.log('Error:', e)
  }
})