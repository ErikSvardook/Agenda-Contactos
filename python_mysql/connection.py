# connection.py
# -----------------------------------------------------------------------------
# Este módulo solo tiene UNA responsabilidad: crear la conexión a MySQL.
# Es la "capa de acceso a datos" del proyecto: clientes.py la usa para
# ejecutar sus consultas y python_mysql.py la usa para levantar la interfaz.
# -----------------------------------------------------------------------------
import os
import mysql.connector
from dotenv import load_dotenv  # Lee el .env y carga sus valores en os.environ
# Importamos la librería "mysql-connector-python".
# Esta librería es el puente entre Python y MySQL: permite abrir conexiones,
# crear cursores y ejecutar sentencias SQL desde código Python.

class CConnection:
    load_dotenv()
    # Clase contenedora de la conexión a la base de datos.
    # Se escribe "CConnection" siguiendo la convención del proyecto
    # (prefijo "C" = Clase, como CClientes).
    # No se instancia; sus métodos se llaman de forma estática, es decir:
    #   CConnection.connectionBaseDeDatos()

    def connectionBaseDeDatos():
        # Método que abre y devuelve una conexión a la base de datos "clientesdb".
        # Idea clave: cada operación (listar, insertar, actualizar, borrar) pide
        # su propia conexión, hace su trabajo y la cierra al final.
        # Así evitamos dejar conexiones abiertas sin usar.

        try:
            # 1) Intentar conectarnos a MySQL con los datos de acceso.
            #    Parámetros de mysql.connector.connect:
            #      user      usuario de MySQL, por defecto "root"
            #      password  la contraseña leída del .env
            #      host      "127.0.0.1" es la máquina local
            #      database  nombre de la BD, por defecto "clientesdb"
            #      port      puerto de MySQL, por defecto 3306

            #os.environ.get("CLAVE", "valor por defecto") lee la variable
            #Si no existe, usa el valor por defecto en lugar de fallar
            conexion = mysql.connector.connect(user=os.environ.get("DB_USER", "root"), password=os.environ.get("DB_PASSWORD", ""), host=os.environ.get("DB_HOST", "127.0.0.1"), database=os.environ.get("DB_NAME", "clientesdb"), port=os.environ.get("DB_PORT", "3306"))
            return conexion
            # Si todo salió bien, devolvemos el objeto "conexion" a quien lo pidió.

        except mysql.connector.Error as error:
            # 2) Si algo falla (BD caída, contraseña mala, puerto equivocado...),
            #    capturamos el error de MySQL y lo mostramos en consola.

            # Devolvemos None para indicar que no hay conexión.
            # clientes.py comprueba este valor antes de usar el cursor.
            print("Error al conectarte a la base de datos: {}".format(error))
            return None

# La conexión se abre solo cuando un método la pide, no al importar el módulo.