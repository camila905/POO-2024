import mysql.connector

try:
#Conexioncon la base de datos de MySQL
conexion=mysql.connector.connect(
    host="loalhost",
    user="root",
    password=""
)

    #Crear un objeto nuevo de tipo cursos para ejecutar SQL
    micursos=conexion.cursor()

    sql="create database bd_python"

    micursor.exacute(sql)


except Exception as e:
    print(F"Error: {e}")
    print(f"Tipo de error: {type(e).__name__}")
    print(f"Ocurrio un eeror por facor vuelva a intentar ... mas tarde ...")
else:
#verificar si la conexion es correcta
if conexion.is_connected():
    print(F"Se creo la conexio existente ...")
else:
    print(f"Se creo la BD exitosamente")
    micursor.execute("show databases")
        print(X)
