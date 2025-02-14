from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from datetime import date

app = FastAPI()

# Modelo de datos
class Tarea(BaseModel):
    id: int
    titulo: str
    descripcion: str
    vencimiento: date
    estado: str  # "completada" o "no completada"

# Base de datos temporal con dos tareas de ejemplo
tareas_db: List[Tarea] = [
    Tarea(id=1, titulo="Estudiar para el examen", descripcion="Repasar los apuntes de TAI", vencimiento=date(2024, 2, 14), estado="completada"),
    Tarea(id=2, titulo="Terminar proyecto de programación", descripcion="Implementar las funciones de la API", vencimiento=date(2024, 2, 20), estado="no completada")
]

# Obtener todas las tareas
@app.get("/tareas", response_model=List[Tarea])
def obtener_tareas():
    return tareas_db

# Obtener una tarea específica por su ID
@app.get("/tareas/{tarea_id}", response_model=Optional[Tarea])
def obtener_tarea(tarea_id: int):
    for tarea in tareas_db:
        if tarea.id == tarea_id:
            return tarea
    return None

# Crear una nueva tarea
@app.post("/tareas", response_model=Tarea)
def crear_tarea(tarea: Tarea):
    tareas_db.append(tarea)
    return tarea

# Actualizar una tarea existente
@app.put("/tareas/{tarea_id}", response_model=Tarea)
def actualizar_tarea(tarea_id: int, tarea_actualizada: Tarea):
    for i, tarea in enumerate(tareas_db):
        if tarea.id == tarea_id:
            tareas_db[i] = tarea_actualizada
            return tarea_actualizada
    return None

# Eliminar una tarea
@app.delete("/tareas/{tarea_id}")
def eliminar_tarea(tarea_id: int):
    global tareas_db
    tareas_db = [t for t in tareas_db if t.id != tarea_id]
    return {"mensaje": "Tarea eliminada correctamente"}
