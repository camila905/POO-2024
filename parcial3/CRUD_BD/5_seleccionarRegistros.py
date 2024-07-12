from conexionBD import *

try:
    micursor=conexion.cursor()
    sql="select * from clientes"

    micursor.execute(sql)

    resultado=micursor.fetchall()

    for fila in resultado:
        print(f"Id:{fila[0]}  Nombre:{fila[1]}  Direccion:{}")


    
    micursor.execute(sql)
    #es necesario ejecutar el comit para que finalice el SQL con exito
    conexion.commit()
except:
    print(f"Ocurrio un error por favor vuelvva a intentar ... mas tarde...")
else:
    print("Se creo la tabla con exito")