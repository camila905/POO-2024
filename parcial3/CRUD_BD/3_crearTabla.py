from conexionBD import *

try:
    micursor=conexion.cursor()
    sql="create table clientes(id int primary key auto_increment, nombre varchar (60), dirreccion varchar(120),tel varchar(10))"

    
    micursor.execute(sql)
except:
    print(f"Ocurrio un error por favor vuelvva a intentar ... mas tarde...")
else:
    print("Se creo la tabla con exito")