# Carrito de Compras - Backend API

Aplicación backend desarrollada con Flask que expone una API RESTful 
para gestionar un carrito de compras de una tienda de gatitos.

## Tecnologías
- Python
- Flask
- Flasgger (Swagger)

## Instalación
pip install flask flasgger

## Cómo ejecutar
python app.py

El servidor queda corriendo en http://localhost:5000

## Documentación Swagger
http://localhost:5000/apidocs

---

## Endpoints

### Productos
| Método | URL | Descripción | Status |
|--------|-----|-------------|--------|
| GET | /products | Listar productos disponibles | 200 |

### Carrito
| Método | URL | Descripción | Status |
|--------|-----|-------------|--------|
| GET | /cart | Ver contenido del carrito | 200 |
| POST | /cart | Agregar producto al carrito | 201 |
| DELETE | /cart/{id} | Eliminar producto del carrito | 200 |
| GET | /cart/total | Calcular total de la compra | 200 |

---

## Probar desde terminal (VSCode - PowerShell)

### Listar productos
Invoke-RestMethod -Uri http://localhost:5000/products -Method GET

### Ver carrito
Invoke-RestMethod -Uri http://localhost:5000/cart -Method GET

### Agregar producto
Invoke-RestMethod -Uri http://localhost:5000/cart -Method POST -ContentType "application/json" -Body '{"id": 1}'

### Ver total
Invoke-RestMethod -Uri http://localhost:5000/cart/total -Method GET

### Eliminar producto
Invoke-RestMethod -Uri http://localhost:5000/cart/1 -Method DELETE

### Error 404 - producto inexistente
Invoke-RestMethod -Uri http://localhost:5000/cart -Method POST -ContentType "application/json" -Body '{"id": 99}'

---

## Probar desde Swagger
1. Levantar el servidor: python app.py
2. Abrir en el navegador: http://localhost:5000/apidocs
3. Hacer click en el endpoint deseado
4. Click en "Try it out"
5. Completar parámetros si corresponde
6. Click en "Execute"

---

## Tests
python test_app.py

Resultado esperado: 8 tests OK