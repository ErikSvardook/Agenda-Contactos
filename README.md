# Agenda de contactos

Aplicación de escritorio en Python con Tkinter para gestionar clientes en una base de datos MySQL. Desde la ventana se pueden agregar, consultar, modificar y eliminar registros.

## Requisitos

- Python 3.12 o 3.13
- MySQL en funcionamiento con la base de datos `clientesdb`
- Librerías `mysql-connector-python` y `python-dotenv`

## Base de datos

El archivo `python_mysql/Script de la base de datos.sql` crea la base de datos `clientesdb` y la tabla `usuarios`, con estas columnas:

    id         int auto_increment primary key not null
    nombres    varchar(50)
    apellidos  varchar(50)
    sexo       varchar(20)
    telefono   varchar(10)

## Configuración

Las credenciales de MySQL se leen desde un archivo `.env` ubicado en la raíz del proyecto. Ese archivo está excluido del repositorio.

    DB_HOST=127.0.0.1
    DB_PORT=3306
    DB_USER=root
    DB_PASSWORD=tu_contraseña
    DB_NAME=clientesdb

## Ejecución

Ubicado en la carpeta `python_mysql`:

```bash
python --version                                            # 1) confirmar que Python existe
python -m pip install mysql-connector-python python-dotenv  # 2) instalar las librerías
python python_mysql.py                                      # 3) arrancar el programa
```

Si se ejecuta desde la raíz del repositorio, el último comando es `python python_mysql/python_mysql.py`.

## Archivos

- `python_mysql.py` construye la ventana y conecta los botones con las operaciones.
- `clientes.py` contiene las operaciones sobre la tabla `usuarios`.
- `connection.py` abre la conexión a MySQL con los datos del `.env`.
