from flask import session
from bd import * 

#https://pynative.com/python-mysql-database-connection/
#https://pynative.com/python-mysql-select-query-to-fetch-data/


#creando una funcion y dentro de la misma una data (un diccionario)
#con valores del usuario ya logueado
def dataLoginSesion():
    inforLogin = {
        "idLogin"             :session['id'],
        "tipoLogin"           :session['tipo_user'],
        "nombre"              :session['nombre'],
        "apellido"            :session['apellido'],
        "emailLogin"          :session['email'],
        "sexo"                :session['sexo'],
        "pais"                      :session['pais'],
        "create_at"                 :session['create_at'],
        "te_gustan_los_videojuegos"  :session['te_gustan_los_videojuegos']
    }
    return inforLogin


def listaPaises():
    conexion_MySQLdb = connectionBD() #Hago instancia a mi conexion desde la funcion
    mycursor       = conexion_MySQLdb.cursor(dictionary=True)
    querySQL  = ("SELECT * FROM paises")
    mycursor.execute(querySQL)
    paises = mycursor.fetchall() #fetchall () Obtener todos los registros
    mycursor.close() #cerrrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD
    return paises

def dataPerfilUsuario():
    conexion_MySQLdb = connectionBD() 
    mycursor       = conexion_MySQLdb.cursor(dictionary=True)
    idUser         = session['id']
    
    querySQL  = ("SELECT * FROM usuarios WHERE id='%s'" % (idUser,))
    mycursor.execute(querySQL)
    datosUsuario = mycursor.fetchone() 
    mycursor.close() #cerrrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD
    return datosUsuario
