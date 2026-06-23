const express = require('express')
const app = express()

app.set('nombre', 'pweb2')
app.set('puerto', 3000)
app.set('case sensitive routing', true) // /Perfil y /perfil serían rutas distintas

app.get('/', (req, res) => {
  res.send(`App: ${app.get('nombre')}`)
})

app.listen(app.get('puerto'), () => console.log('Servidor en http://localhost:3000'))