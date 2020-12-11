#Definicion de usuario en la Base de datos
from typing import Dict
from pydantic import BaseModel
from datetime import date

class usuarioDB(BaseModel):
    usuario: str
    contrasena: str
    nombre_completo: str
    fecha_nacimiento: date
    email: str
    tipo_documento: str
    cedula: str

# definición de la base de datos ficticia

basededatos_usuario = Dict[str, usuarioDB]

basededatos_usuario = {
    "diegoVega25": usuarioDB(**{"usuario":"diegoVega25",
                                "contrasena":"1234",
                                "nombre_completo":"Diego Vega",
                                "fecha_nacimiento": 12/24/1985,
                                "email":"diegoVega25@gmail.com",
                                "tipo_documento":"CC",
                                "cedula":"1094256896"}),

    "andresNieto32": usuarioDB(**{"usuario":"andresNieto32",
                                "contrasena":"5678",
                                "nombre_completo":"Andres Nieto",
                                "fecha_nacimiento": 2/20/1975,
                                "email":"andresNieto32@hotmail.com",
                                "tipo_documento":"CC",
                                "cedula":"80025986"}),
}
                                


#definición de funciones sobre la base de datos fictica

#llama al usuario si existe, y retorna los datos
def get_usuario(usuario: str):
    if usuario in basededatos_usuario.keys():
        return basededatos_usuario[usuario]
    else:
        return None

#Actualiza o crea el nuevo usuario en la base de datos
def update_usuario(nuevo_usuario: usuarioDB):
    basededatos_usuario[nuevo_usuario.usuario] = nuevo_usuario
    return nuevo_usuario