from pymongo import MongoClient

cliente = MongoClient('mongodb://127.0.0.1:27017')
#acciendo a mi base de datos
db = cliente['codigog4']

colAlumnos = db['alumnos']

#alumnoId = colAlumnos.insert_one({"nombre":"Cecilia Amado","email":"camado@yahoo.es","dni":"234234","edad":40})
#print(alumnoId)
for a in colAlumnos.find():
    print(a["nombre"] + " - " + a["email"])