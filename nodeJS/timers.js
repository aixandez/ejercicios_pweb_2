// Se ejecuta UNA sola vez después de 2 segundos
setTimeout(() => {
  console.log('Hola desde setTimeout')
}, 2000)

// Se ejecuta cada 1 segundo (presioná Ctrl+C para detenerlo)
setInterval(() => {
  console.log('Hola desde setInterval')
}, 1000)