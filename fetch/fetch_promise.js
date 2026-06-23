// Versión con promesas (.then)
// Hace un pedido a la URL y cuando llegan los datos los convierte a JSON y los muestra
fetch("https://jsonplaceholder.typicode.com/posts")
  .then((res) => res.json())
  .then((data) => console.log(data))
  .catch((error) => console.log(error))