from conexionBD import *

try:
    micursor=conexion.cursor()
    sql="update clientes set dirreccion="col. del "UTD" WHERE id=11"


    micursor.execute(sql)
    #es necesario ejecutar el comit para que finalice el SQL con exito
    conexion.commit()
except:
    print(f"Ocurrio un error por favor vuelvva a intentar ... mas tarde...")
else:
    print("Registro Eliminado con Exito")