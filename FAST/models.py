from pydantic import BaseModel, Field

class modelUsuario(BaseModel):
    id:int = Field(...,gt=0, description="Id siempre debe ser positivo")
    nombre:str = Field(...,min_length=1, max_length=85 ,description=" solo letras y espacios min 1 max 85")
    edad:int = Field(..., gt=0, ge=120, description="Edad debe estar entre 0 y 120 años")
    correo: str = Field(..., pattern=r"^.@.com$", example="usuario@example.com", description="Correo válido") 