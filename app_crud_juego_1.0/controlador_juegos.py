"""
CRUD FLASK PYTHON + MYSQL
Desarrollado por: Ever Canchano
"""

# Realizamos la importación de nuestra función de conexión
from db import obtener_conexion

# Controlador: insertar_juego
def insertar_juego(nombre, descripcion, precio):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "INSERT INTO juegos(nombre, descripcion, precio) VALUES (%s, %s, %s)",
            (nombre, descripcion, precio)
        )
    conexion.commit()
    conexion.close()

# Controlador: obtener_juego
def obtener_juegos():
    conexion = obtener_conexion()
    juegos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre, descripcion, precio FROM juegos")
        juegos = cursor.fetchall()
    conexion.close()
    return juegos

# Controlador: obtener juego por ID
def obtener_juego_por_id(id):
    # Obtener una conexión a la base de datos
    conexion = obtener_conexion()

    # Inicializar una variable para almacenar el juego
    juego = None

    # Crear un cursor para ejecutar las consultas SQL
    with conexion.cursor() as cursor:
        # Ejecutar la consulta para obtener el juego por su ID
        cursor.execute("SELECT id, nombre, descripcion, precio FROM juegos WHERE id = %s", (id,))
        # Obtener el primer resultado (solo debería haber uno)
        juego = cursor.fetchone()

    # Cerrar la conexión a la base de datos
    conexion.close()

    # Retornar el juego encontrado (o None si no existe)
    return juego

# Controlador: actualizar juego
def actualizar_juego(nombre, descripcion, precio, id):
    # Obtener una conexión a la base de datos
    conexion = obtener_conexion()

    # Crear un cursor para ejecutar las consultas SQL
    with conexion.cursor() as cursor:
        # Ejecutar la consulta para actualizar el juego
        cursor.execute("UPDATE juegos SET nombre = %s, descripcion = %s, precio = %s WHERE id = %s",
                        (nombre, descripcion, precio, id))
        # Confirmar los cambios en la base de datos
        conexion.commit()

    # Cerrar la conexión a la base de datos
    conexion.close()

# Controlador: eliminar juego
def eliminar_juego(id):
    # Obtener una conexión a la base de datos
    conexion = obtener_conexion()

    # Crear un cursor para ejecutar las consultas SQL
    with conexion.cursor() as cursor:
        # Ejecutar la consulta para eliminar el juego
        cursor.execute("DELETE FROM juegos WHERE id = %s", (id,))
        # Confirmar los cambios en la base de datos
        conexion.commit()

    # Cerrar la conexión a la base de datos
    conexion.close()
