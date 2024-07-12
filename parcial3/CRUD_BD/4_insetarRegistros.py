from conexionBD import *

try:
    micursor=conexion.cursor()
    sql="INSERT INTO clientes values (NULL, nombre, direccion, tel) VALUES (NULL, "Juan Polaina", "Col. del valle", "6181234567")"

    
    micursor.execute(sql)
    #es necesario ejecutar el comit para que finalice el SQL con exito
    conexion.commit()
except:
    print(f"Ocurrio un error por favor vuelvva a intentar ... mas tarde...")
else:
    print("Se creo la tabla con exito")