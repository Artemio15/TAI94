from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI(
    title="Mi primer Api",
    description="Artemio Anaya Martínez",
    version="0.1"
)

usuarios=[
    {"id":1,"nombre":"Artemio","edad":20},
    {"id":2,"nombre":"Miguel","edad":24},
    {"id":3,"nombre":"Gustavi","edad":23},
    {"id":4,"nombre":"Samuel","edad":28},
]

#EndPoint
@app.get("/",tags=["Inicio"])
def home():
    return {"message": "Hello, FastAPI!"}

#EndPoint Consulta
@app.get("/todosusuarios",tags=["Operaciones CRUD"])
def leer():
    return {"Usuarios Registrados":usuarios}

#EndPoint POST
@app.post('/usuarios/',tags=['Operaciones CRUD'])
def guardar(usuario:dict):
    for usr in usuarios:
        if usr["id"]==usuario.get("id"):
            raise HTTPException(status_code=400,detail="El usuario ya existe")
    usuarios.append(usuario)
    return usuario

#EndPoint para actualizar
@app.put('/usuarios/{id}',tags=['Operaciones CRUD'])
def actualizar(id:int,usuarioActualizado:dict):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index].update(usuarioActualizado)
            return usuarios[index]
    raise HTTPException(status_code=400,detail="El usuario no existe")


#EndPoint para eliminar
@app.delete('/usuarios/{id}',tags=['Operaciones CRUD'])
def eliminar(id: int):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios.pop(index)
            return {"message": "Usuario eliminado"}
    raise HTTPException(status_code=404, detail="El usuario no existe")


