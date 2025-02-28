from fastapi import FastAPI, HTTPException
from typing import Optional, List
from pydantic import BaseModel
from models import modelUsuario, modelAuth
from genToken import createToken


app = FastAPI(
    title="Mi primer API con FastAPI",
    description="Esto es una descripción de mi API",
    version="1.0.1"
)
    

usuarios=[
    {"id":1, "nombre":"Daniel", "edad":20, "correo":"d@gmail.com"},
    {"id":2, "nombre":"Miguel", "edad":20, "correo":"m@gmail.com"},
    {"id":3, "nombre":"Luis", "edad":20, "correo":"l@gmail.com"},
    {"id":4, "nombre":"Juan", "edad":20, "correo":"j@gmail.com"},
    {"id":5, "nombre":"Pedro", "edad":20, "correo":"p@gmail.com"}

]

@app.get("/", tags=["inicio"])
def home():
    return {"message": "Hello, FastAPI!"}


#Endpoint para generar token
@app.post("/auth", tags=["Autenticacion"])
def auth(credenciales:modelAuth):
    if credenciales.mail == "arte@example.com" and credenciales.passw == "123456789":
        token:str = createToken(credenciales.model_dump())
        print(token)
        return {"token": "Token Generado"}
    else:
        return {"Aviso": "Usuario no cuenta con permiso"}




#Endpoint para obtener todos los usuarios
@app.get("/todosUsuarios", response_model=List[modelUsuario], tags=["Operaciones Crud"])
def leer():
    return usuarios

#Endpoint para obtener todos los usuarios
@app.post("/Usuarios/", response_model=List[modelUsuario], tags=["Operaciones Crud"])
def guardar(usuario:modelUsuario):
    for usr in usuarios:
        if usr["id"] == usuario.id:
            raise HTTPException(status_code=400, detail="El usuario ya existe")
    usuarios.append(usuario)
    return usuario

#Endpoint para obtener un usuario por su id
@app.put("/Usuarios/{id}", response_model=List[modelUsuario], tags=["Operaciones Crud"])
def actualizar(id: int, usuarioActualizado:modelUsuario):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index] = usuarioActualizado.model_dump()
            return usuarios[index]
    raise HTTPException(status_code=400, detail="Usuario no existe")


@app.delete('/usuarios/{id}',tags=['Operaciones CRUD'])
def eliminar(id: int):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            del usuarios[index]
            return {"message": "Usuario eliminado"}
    raise HTTPException(status_code=404, detail="El usuario no existe")