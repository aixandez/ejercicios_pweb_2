// En vez de traer todos los posts, trae solo el que tiene id=1
async function loadPost() {
  try {
    const res = await fetch("https://jsonplaceholder.typicode.com/posts/1")
    const data = await res.json()
    console.log(data)
  } catch (error) {
    console.log(error)
  }
}

loadPost()