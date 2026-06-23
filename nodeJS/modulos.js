const os = require('os')

console.log('Usuario:', os.userInfo().username)
console.log('Plataforma:', os.platform())
console.log('Memoria total (MB):', Math.round(os.totalmem() / 1024 / 1024))
console.log('Memoria libre (MB):', Math.round(os.freemem() / 1024 / 1024))

const fs = require('fs')
fs.writeFileSync('data.txt', 'Programación\nWeb\n2')
const contenido = fs.readFileSync('data.txt', 'utf-8')
console.log(contenido)