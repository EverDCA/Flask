#Realizamos la importacion de la libreria PyMySQL instalado previamente con pip install
import pymysql

#configuramos los datos de conexion con la base de datos
def obtener_conexion():
    return pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='app_crud_juego')