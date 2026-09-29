# Taller para la casa — FastAPI

**Clase 4 · Ficha 3231102 (ADSO — SENA)**

Vas a construir una pequeña API para un **catálogo de libros**. Es la misma
idea que hicimos en clase con los aprendices, pero aplicada a un tema nuevo:
eso es justo lo que te ayuda a afianzar FastAPI. Trabaja sobre el archivo
`taller_fastapi.py` y completa cada `# TODO`.

---

## Cómo ponerlo a correr

```bash
# 1. Activa tu entorno virtual
python -m venv venv
source venv/bin/activate        # En Windows:  venv\Scripts\activate

# 2. Instala FastAPI
pip install "fastapi[standard]"

# 3. Arranca el servidor
uvicorn taller_fastapi:app --reload

# 4. Abre en el navegador
#    http://127.0.0.1:8000/docs
```

Puedes correrlo desde el principio: cada endpoint irá **apareciendo en /docs**
a medida que lo completes. Prueba cada uno con el botón **"Try it out"**.

---

## Los ejercicios

| # | Endpoint | Concepto | Cómo probarlo |
|---|----------|----------|---------------|
| 1 | `GET /` | Primer endpoint | Abrir `/` en el navegador |
| 2 | `GET /libros` | Devolver una lista | Abrir `/libros` |
| 3 | `GET /libros/{id}` | Parámetro de **ruta** | Abrir `/libros/1` |
| 4 | `GET /buscar?anio=` | Parámetro de **consulta** | Abrir `/buscar?anio=1967` |
| 5 | `POST /libros` | Crear + validar con Pydantic | Desde `/docs` → "Try it out" |

### Reto opcional (para nota máxima)

| # | Endpoint | Concepto |
|---|----------|----------|
| 6 | `PUT /libros/{id}` | Actualizar un libro |
| 7 | `DELETE /libros/{id}` | Eliminar un libro |

---

## Pistas rápidas

- Para buscar un libro por su id, **recorre la lista con un `for`** y compara
  `libro["id"] == id`.
- Para crear un libro con `POST`, convierte el modelo a diccionario con
  `nuevo.model_dump()` y asígnale un id nuevo (por ejemplo `len(libros) + 1`).
- **`POST`, `PUT` y `DELETE` no se prueban desde la barra del navegador**
  (esa solo hace `GET`). Úsalos desde `/docs`.

---

## Qué entregar

Sube tu archivo `taller_fastapi.py` completado al repositorio del curso.

**Criterio:** que al abrir tu `/docs` se puedan probar los endpoints 1 a 5
funcionando correctamente. El reto (6 y 7) suma para la nota máxima.
