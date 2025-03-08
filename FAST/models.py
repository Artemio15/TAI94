from pydantic import BaseModel, Field, EmailStr

class modelUsuario(BaseModel):
    id:int = Field(...,gt=0, description="Id siempre debe ser positivo")
    nombre:str = Field(...,min_length=1, max_length=85 ,description=" solo letras y espacios min 1 max 85")
    edad:int = Field(..., gt=0, description="Edad debe estar entre 0 y 120 años")
    correo: str = Field(..., description="Correo válido") 

class modelAuth(BaseModel):
    mail:EmailStr 
    passw:str = Field(...,min_length=8, strip_whitespace= True ,description=" solo letras sin espacios min 8")



