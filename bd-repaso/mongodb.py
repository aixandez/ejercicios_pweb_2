import pymongo

# Conectarse a MongoDB local
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb['customers']

# Limpiar colección para poder correr el script varias veces
mycol.delete_many({})

# Insertar un documento
x = mycol.insert_one({ "name": "John", "address": "Highway 37" })
print('ID insertado:', x.inserted_id)

# Insertar muchos documentos
mylist = [
    { "_id": 1, "name": "Peter", "address": "Lowstreet 27"},
    { "_id": 2, "name": "Amy", "address": "Apple st 652"},
    { "_id": 3, "name": "Hannah", "address": "Mountain 21"},
    { "_id": 4, "name": "Michael", "address": "Valley 345"},
    { "_id": 5, "name": "Sandy", "address": "Ocean blvd 2"},
    { "_id": 6, "name": "Susan", "address": "Sky st 331"},
    { "_id": 7, "name": "Ben", "address": "Park Lane 38"},
]
x = mycol.insert_many(mylist)
print('IDs insertados:', x.inserted_ids)

# Primer documento
print('\nPrimer documento:', mycol.find_one())

# Todos
print('\nTodos:')
for x in mycol.find():
    print(x)

# Solo nombre y dirección sin _id
print('\nSolo nombre y dirección:')
for x in mycol.find({}, { "_id": 0, "name": 1, "address": 1 }):
    print(x)

# Filtro exacto
print('\nPark Lane 38:')
for x in mycol.find({ 'address': 'Park Lane 38' }):
    print(x)

# Filtro con $gt
print('\nDirecciones > S:')
for x in mycol.find({ 'address': { '$gt': 'S' } }):
    print(x)

# Filtro con regex
print('\nDirecciones que empiezan con S:')
for x in mycol.find({ 'address': { '$regex': '^S' } }):
    print(x)

# Ordenar A-Z
print('\nOrdenado A-Z:')
for x in mycol.find().sort('name'):
    print(x)

# Ordenar Z-A
print('\nOrdenado Z-A:')
for x in mycol.find().sort('name', -1):
    print(x)

# Actualizar
mycol.update_one({ 'address': 'Valley 345' }, { '$set': { 'address': 'Canyon 123' } })
print('\nDespués de actualizar Valley 345:')
for x in mycol.find():
    print(x)

# Eliminar uno
mycol.delete_one({ 'address': 'Mountain 21' })
print('\nDespués de eliminar Mountain 21:')
for x in mycol.find():
    print(x)

# Limitar
print('\nPrimeros 3:')
for x in mycol.find().limit(3):
    print(x)