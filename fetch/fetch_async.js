// Versión con async/await
// Espera a que lleguen los datos antes de continuar, como si fuera código sincrónico
async function loadData() {
  try {
    const res = await fetch("https://jsonplaceholder.typicode.com/posts")
    const data = await res.json()
    console.log(data)
  } catch (error) {
    console.log(error)
  }
}

loadData()