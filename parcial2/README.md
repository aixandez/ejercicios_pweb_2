LINK AL PRIMER PARCIAL: https://github.com/aixandez/ejercicios_pweb_2/tree/main/parcial_proyecto
LINK AL SEGUNDO PARCIAL: https://github.com/aixandez/ejercicios_pweb_2/tree/main/parcial2



El proyecto consiste en una aplicación web de tipo Single Page Application (SPA) inspirada en Coffee Cart, adaptada como un carrito de compras de gatitos. Se desarrolló en las dos etapas pedidas: la primera enfocada en el backend con APIs RESTful, y la segunda incorporando el frontend, una base de datos y pruebas E2E automatizadas.



ARQUITECTURA ELEGIDA:

Se utilizó una arquitectura cliente-servidor de dos capas:


Backend: servidor Flask (Python) que expone una API RESTful con cinco endpoints. Gestiona la lógica del negocio y la comunicación con la base de datos SQLite.

Frontend: página HTML vainilla que se sirve desde el mismo servidor Flask. Consume la API mediante fetch con async/await y actualiza el DOM dinámicamente sin recargar la página.

El flujo de la aplicación es el siguiente: el usuario interactúa con la interfaz HTML, el JavaScript del frontend realiza peticiones HTTP al backend Flask, Flask consulta o modifica la base de datos SQLite y devuelve una respuesta en formato JSON, que el frontend usa para actualizar la pantalla."),
 


TECNOLOGÍAS UTILIZADAS:

Primer parcial (Backend): Flask, python, flassger, unittest.
Segundo parcial (Frontend + base de datos + pruebas E2E): HTML + css + JavaScript, Selenium, SQLite, fetch.



DIFICULTADES ENCONTRADAS:
Al comenzar la segunda etapa del proyecto, mi principal dificultad fue entender cómo continuar a partir del primer parcial. No tenía claro si debía reutilizar el código existente o rehacer la aplicación con una estructura diferente. Para resolver esta duda utilicé inteligencia artificial como herramienta de apoyo y ahí entendí que debía trabajar a partir de lo que había hecho en el parcial anterior.

También tuve dificultades con la incorporación de la base de datos, ya que tenía poca experiencia con SQL y ya había tenido inconvenientes con las instalaciones (antes usaba sqlite online cuando veía postgresql). Por ello opté por utilizar SQLite, ya que pude trabajar fácilmente la base de datos desde Visual Studio Code.

Por último, durante las pruebas E2E con Selenium surgió un problema porque los productos agregados por un test permanecían en el carrito para los siguientes test, provocando errores. Por ejemplo en el test de flujo de compra completo puse agregar dos productos y verificar que en el carrito quedaran dos productos, y me dio error porque tenía más productos de los anteriores tests. Para solucionarlo agregué un endpoint DELETE /cart que vacía el carrito antes de ejecutar cada prueba, garantizando que todos los tests comienzan con el carrito vacío.
