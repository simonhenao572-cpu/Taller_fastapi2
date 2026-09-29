"""
==========================================================================
 TALLER PARA LA CASA — FastAPI
 Clase 4 · Ficha 3231102 (ADSO - SENA)
==========================================================================

 Tema: una pequena API para un CATALOGO DE LIBROS.

 Idea del taller: en clase construimos la API de "aprendices". Aqui vas a
 construir la MISMA idea pero con "libros". Aplicar lo aprendido a un tema
 nuevo es lo que de verdad afianza el conocimiento. No copies y pegues:
 vuelve a pensarlo.

 Como trabajar:
   1. Activa tu entorno virtual.
   2. Instala FastAPI:     pip install "fastapi[standard]"
   3. Corre el servidor:   uvicorn taller_fastapi:app --reload
   4. Abre en el navegador: http://127.0.0.1:8000/docs
   5. Completa cada  # TODO  y prueba cada endpoint desde /docs.

 Puedes correr el archivo desde el primer momento: iras viendo aparecer
 cada endpoint en /docs a medida que lo completes.
==========================================================================
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# --------------------------------------------------------------------------
#  "Base de datos" temporal en memoria  (ya esta lista)
#  Recuerda: al reiniciar el servidor, estos datos vuelven a su estado inicial.
# --------------------------------------------------------------------------
libros = [
    {"id": 1, "titulo": "Cien anios de soledad", "anio": 1967},
    {"id": 2, "titulo": "El Quijote", "anio": 1605},
]

# Molde de validacion para crear libros (ya esta listo)
class Libro(BaseModel):
    titulo: str
    anio: int


# ==========================================================================
#  EJERCICIO 1 — Endpoint de bienvenida        (GET /)
#  Objetivo: devolver un mensaje de bienvenida.
#  Prueba:   http://127.0.0.1:8000/   ->   {"mensaje": "..."}
# ==========================================================================
# TODO: crea un endpoint GET en la ruta "/" con una funcion que
#       retorne un diccionario de bienvenida, por ejemplo:
#       {"mensaje": "Bienvenido al catalogo de libros"}
@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido al catalogo de libros"}


# ==========================================================================
#  EJERCICIO 2 — Listar todos los libros        (GET /libros)
#  Objetivo: devolver la lista completa de libros.
#  Prueba:   /libros   ->   la lista en formato JSON
# ==========================================================================
# TODO: crea un endpoint GET en "/libros" que retorne la lista 'libros'.
@app.get("/libros")
def listar():
    return libros


# ==========================================================================
#  EJERCICIO 3 — Un libro por su id           (parametro de RUTA)
#  Objetivo: /libros/1 debe devolver SOLO el libro con id = 1.
#  Pista:    recorre la lista con un for y compara  libro["id"] == id
# ==========================================================================
# TODO: crea GET "/libros/{id}" con el parametro  id: int.
#       - Si encuentras el libro, retornalo.
#       - Si no existe, retorna  {"error": "Libro no encontrado"}
@app.get("/libros/{id}")
def obtener(id: int):
    for libro in libros:
        if libro["id"] == id:
            return libro
    return {"error": "Libro no encontrado"}


# ==========================================================================
#  EJERCICIO 4 — Buscar por anio             (parametro de CONSULTA)
#  Objetivo: /buscar?anio=1967 devuelve los libros de ese anio.
#  Pista:    define la funcion como  def buscar(anio: int = 0)
#            y arma una lista con los libros cuyo "anio" coincida.
# ==========================================================================
# TODO: crea GET "/buscar" que reciba el parametro de consulta ?anio=
#       y devuelva SOLO los libros de ese anio.
@app.get("/buscar")
def buscar(anio: int = 0):
    resultado = []
    for libro in libros:
        if libro["anio"] == anio:
            resultado.append(libro)
    return resultado


# ==========================================================================
#  EJERCICIO 5 — Crear un libro               (POST + Pydantic)
#  Objetivo: recibir un libro validado y agregarlo a la lista.
#  Pista:    usa  nuevo.model_dump()  para convertirlo en diccionario.
#            Asigna un id nuevo, por ejemplo  len(libros) + 1
# ==========================================================================
# TODO: crea POST "/libros" que reciba  nuevo: Libro,  le asigne un id,
#       lo agregue a la lista y devuelva el libro creado.
@app.post("/libros")
def crear(nuevo: Libro):
    # max()+1 en vez de len()+1: asi el id no se repite si ya borraste libros
    nuevo_id = max((l["id"] for l in libros), default=0) + 1
    libro = {"id": nuevo_id, **nuevo.model_dump()}
    libros.append(libro)
    return libro


# ==========================================================================
#  RETO OPCIONAL (para nota maxima) — Completar el CRUD
#  Solo si terminaste lo anterior. Aqui aplicas PUT y DELETE.
# ==========================================================================
# TODO (reto): PUT "/libros/{id}"    -> actualizar titulo y anio de un libro.
@app.put("/libros/{id}")
def actualizar(id: int, datos: Libro):
    for libro in libros:
        if libro["id"] == id:
            libro["titulo"] = datos.titulo
            libro["anio"] = datos.anio
            return libro
    return {"error": "Libro no encontrado"}
# TODO (reto): DELETE "/libros/{id}" -> eliminar un libro de la lista.
@app.delete("/libros/{id}")
def eliminar(id: int):
    for libro in libros:
        if libro["id"] == id:
            libros.remove(libro)
            return {"mensaje": "Libro eliminado"}
    return {"error": "Libro no encontrado"}


# --------------------------------------------------------------------------
#  Nota: para probar POST, PUT y DELETE NO uses la barra del navegador
#  (esa solo hace GET). Usa la pagina /docs con el boton "Try it out".
# --------------------------------------------------------------------------
