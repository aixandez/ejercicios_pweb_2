// Trae la lista de usuarios y filtra solo los datos que nos interesan
async function loadUsuarios() {
  try {
    const res = await fetch("https://jsonplaceholder.typicode.com/users")
    const data = await res.json()
    data.forEach((usuario) => {
      console.log(`Nombre: ${usuario.name} - Email: ${usuario.email}`)
    })
  } catch (error) {
    console.log(error)
  }
}

loadUsuarios()