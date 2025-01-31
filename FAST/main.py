from fastapi import FastAPI
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

#EndPoint
@app.get("/promedio",tags=["Mi calificacion TAI"])
def promedio():
    return 10.5

#EndPoint
@app.get("/usuario/{id}",tags=["Endpoint parametro obligatorio"])
def consultausuario(id: int):
    return {"Se encontro el usuario":id}

#EndPoint
@app.get("/usuario/",tags=["Endpoint parametro opcional"])
def consultausuario2(id: Optional[int]=None):
    if id is not None:
        for usuario in usuarios:
            if usuario["id"]==id:
                return {"mensaje":"usuario encontrado","El usuario es":usuario}
        return {"mensaje":f"No se encontro el id{id}"}
    return{"mensaje":"No se proporciono un id"}
        

#endpoint con varios parametro opcionales
@app.get("/usuarios/", tags=["3 parámetros opcionales"])
async def consulta_usuarios(
    usuario_id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:
        if (
            (usuario_id is None or usuario["id"] == usuario_id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}
