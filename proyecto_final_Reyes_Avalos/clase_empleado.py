#clase empleado 

class Empleado:
    def __init__(self, id_empleado, nombre, telefono):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.telefono = telefono

    def registrar_empleado(self):
        print(f"Empleado registrado: {self.nombre}, ID: {self.id_empleado}, Teléfono: {self.telefono}")

    def procesar_venta(self, medicamentos):
        fecha_ventas = "2024-08-11 10:30:00"
        id_ventas = 1
        venta = Ventas(id_ventas, fecha_ventas)

        for medicamento, cantidad in medicamentos:
            venta.registrar_venta(medicamento, cantidad)

        id_factura = 1
        numero_factura = "F20240811103000"
        factura = venta.generar_factura(id_factura, numero_factura)
        factura.imprimir(venta.ventas)
    
        
        
empleado1 = Empleado(1, "Raul", "+6183679990")
empleado1.registrar_empleado()

class Empleado:
    def __init__(self, id_empleado, nombre, telefono):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.telefono = telefono

    def registrar_empleado(self):
        conexion = conectar_bd()
        if conexion:
            try:
                cursor = conexion.cursor()
                sql = "INSERT INTO empleados (id_empleado, nombre, telefono) VALUES (%s, %s, %s)"
                cursor.execute(sql, (self.id_empleado, self.nombre, self.telefono))
                conexion.commit()
                messagebox.showinfo("Registro Exitoso", f"Empleado {self.nombre} registrado en la base de datos con éxito.")
            except mysql.connector.Error as err:
                messagebox.showerror("Error al Registrar", f"No se pudo registrar el empleado: {err}")
            finally:
                conexion.close()