import mysql.connector

def conectar_db():
    conexion = mysql.connector.connect(
        host="localhost",  # Cambia esto si es diferente
        user="tu_usuario",  # Cambia esto a tu usuario de MySQL
        password="tu_contraseña",  # Cambia esto a tu contraseña de MySQL
        database="sistema_de_farmacos_controlados"  # Cambia esto a tu nombre de base de datos
    )
    return conexion

def borrarPantalla():
    os.system('cls')

def esperarTecla():
    input("Presiona cualquier tecla para continuar...")

class Factura:
    def __init__(self, id_factura, numero_factura, fecha_emision, id_ventas):
        self.id_factura = id_factura
        self.numero_factura = numero_factura
        self.fecha_emision = fecha_emision
        self.id_ventas = id_ventas

    def guardar_en_db(self, conexion):
        cursor = conexion.cursor()
        sql = "INSERT INTO factura (id_factura, numero_factura, fecha_emision, id_ventas) VALUES (%s, %s, %s, %s)"
        valores = (self.id_factura, self.numero_factura, self.fecha_emision, self.id_ventas)
        cursor.execute(sql, valores)
        conexion.commit()

    def imprimir(self, ventas):
        print("\n===== Factura =====")
        print(f"ID Factura: {self.id_factura}")
        print(f"Número de Factura: {self.numero_factura}")
        print(f"Fecha de Emisión: {self.fecha_emision}")
        total = 0
        for venta in ventas:
            print(f"\nMedicamento: {venta['medicamento'].nombre}")
            print(f"Cantidad: {venta['cantidad']}")
            print(f"Subtotal: {venta['subtotal']}")
            total += venta['subtotal']
        print(f"\nTotal a Pagar: {total}")
        print("===================\n")


class Ventas:
    def __init__(self, id_ventas, fecha_ventas, id_cliente, id_empleado):
        self.id_ventas = id_ventas
        self.fecha_ventas = fecha_ventas
        self.id_cliente = id_cliente
        self.id_empleado = id_empleado
        self.ventas = []

    def guardar_en_db(self, conexion):
        cursor = conexion.cursor()
        sql = "INSERT INTO ventas (id_ventas, fecha_venta, id_cliente, id_empleado) VALUES (%s, %s, %s, %s)"
        valores = (self.id_ventas, self.fecha_ventas, self.id_cliente, self.id_empleado)
        cursor.execute(sql, valores)
        conexion.commit()

    def registrar_venta(self, conexion, medicamento, cantidad):
        subtotal = medicamento.precio * cantidad
        self.ventas.append({
            'medicamento': medicamento,
            'cantidad': cantidad,
            'subtotal': subtotal
        })

        cursor = conexion.cursor()
        sql = "INSERT INTO ventas (id_ventas, id_cliente, id_empleado, id_medicamento, cantidad, subtotal) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (self.id_ventas, self.id_cliente, self.id_empleado, medicamento.id_medicamento, cantidad, subtotal)
        cursor.execute(sql, valores)
        conexion.commit()

    def generar_factura(self, conexion, id_factura, numero_factura):
        factura = Factura(id_factura, numero_factura, self.fecha_ventas, self.id_ventas)
        factura.guardar_en_db(conexion)
        return factura


class Empleado:
    def __init__(self, id_empleado, nombre, telefono):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.telefono = telefono

    def guardar_en_db(self, conexion):
        cursor = conexion.cursor()
        sql = "INSERT INTO empleado (id_empleado, nombre, telefono) VALUES (%s, %s, %s)"
        valores = (self.id_empleado, self.nombre, self.telefono)
        cursor.execute(sql, valores)
        conexion.commit()

    def registrar_empleado(self, conexion):
        print(f"Empleado registrado: {self.nombre}, ID: {self.id_empleado}, Teléfono: {self.telefono}")
        self.guardar_en_db(conexion)

    def procesar_venta(self, conexion, cliente, medicamentos):
        fecha_ventas = "2024-08-11 10:30:00"
        id_ventas = 1  # Este ID debería generarse de manera adecuada, podría ser autoincremental en la base de datos
        venta = Ventas(id_ventas, fecha_ventas, cliente.id_cliente, self.id_empleado)

        venta.guardar_en_db(conexion)

        for medicamento, cantidad in medicamentos:
            venta.registrar_venta(conexion, medicamento, cantidad)

        id_factura = 1  # Este ID debería generarse de manera adecuada, podría ser autoincremental en la base de datos
        numero_factura = "F20240811103000"
        factura = venta.generar_factura(conexion, id_factura, numero_factura)
        factura.imprimir(venta.ventas)


class Proveedor:
    def __init__(self, id_proveedor, nombre, telefono, direccion):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion

    def guardar_en_db(self, conexion):
        cursor = conexion.cursor()
        sql = "INSERT INTO proveedor (id_proveedor, nombre, telefono, direccion) VALUES (%s, %s, %s, %s)"
        valores = (self.id_proveedor, self.nombre, self.telefono, self.direccion)
        cursor.execute(sql, valores)
        conexion.commit()

    def mostrar_informacion(self):
        print(f"ID: {self.id_proveedor}, Nombre: {self.nombre}, Teléfono: {self.telefono}, Dirección: {self.direccion}")

    def actualizar_stock(self, conexion):
        print(f"Actualizando stock del proveedor {self.nombre}")

    def suministrar_medicamento(self):
        print(f"Suministrando medicamento del proveedor {self.nombre}")


class Medicamento:
    def __init__(self, id_medicamento, nombre, precio, stock, id_proveedor):
        self.id_medicamento = id_medicamento
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.id_proveedor = id_proveedor

    def guardar_en_db(self, conexion):
        cursor = conexion.cursor()
        sql = "INSERT INTO medicamento (id_medicamento, nombre, precio, stock, id_proveedor) VALUES (%s, %s, %s, %s, %s)"
        valores = (self.id_medicamento, self.nombre, self.precio, self.stock, self.id_proveedor)
        cursor.execute(sql, valores)
        conexion.commit()

    def actualizar_stock(self, conexion, cantidad):
        self.stock += cantidad
        cursor = conexion.cursor()
        sql = "UPDATE medicamento SET stock = %s WHERE id_medicamento = %s"
        valores = (self.stock, self.id_medicamento)
        cursor.execute(sql, valores)
        conexion.commit()

    def consultar_disponibilidad(self):
        return self.stock > 0

    def mostrar_informacion(self):
        print(f"ID Medicamento: {self.id_medicamento}, Nombre: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}")


class Antibiotico(Medicamento):
    def __init__(self, id_medicamento, nombre, precio, stock, id_proveedor, concentracion_en_ml):
        super().__init__(id_medicamento, nombre, precio, stock, id_proveedor)
        self.concentracion_en_ml = concentracion_en_ml

    def guardar_en_db(self, conexion):
        super().guardar_en_db(conexion)
        cursor = conexion.cursor()
        sql = "INSERT INTO antibiotico (id_antibiotico, concentracion_ml, id_medicamento) VALUES (%s, %s, %s)"
        valores = (self.id_medicamento, self.concentracion_en_ml, self.id_medicamento)
        cursor.execute(sql, valores)
        conexion.commit()

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Concentración en ml: {self.concentracion_en_ml}")


class Antiinflamatorio(Medicamento):
    def __init__(self, id_medicamento, nombre, precio, stock, id_proveedor, concentracion_en_mg):
        super().__init__(id_medicamento, nombre, precio, stock, id_proveedor)
        self.concentracion_en_mg = concentracion_en_mg

    def guardar_en_db(self, conexion):
        super().guardar_en_db(conexion)
        cursor = conexion.cursor()
        sql = "INSERT INTO antiinflamatorio (id_antiinflamatorio, concentracion_mg, id_medicamento) VALUES (%s, %s, %s)"
        valores = (self.id_medicamento, self.concentracion_en_mg, self.id_medicamento)
        cursor.execute(sql, valores)
        conexion.commit()

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Concentración en mg: {self.concentracion_en_mg}")


class Cliente:
    def __init__(self, id_cliente, nombre_cliente, telefono, direccion):
        self.id_cliente = id_cliente
        self.nombre_cliente = nombre_cliente
        self.telefono = telefono
        self.direccion = direccion

    def guardar_en_db(self, conexion):
        cursor = conexion.cursor()
        sql = "INSERT INTO cliente (id_cliente, nombre_cliente, telefono, direccion) VALUES (%s, %s, %s, %s)"
        valores = (self.id_cliente, self.nombre_cliente, self.telefono, self.direccion)
        cursor.execute(sql, valores)
        conexion.commit()

    def solicitar_medicamento(self, conexion, medicamento, cantidad):
        if medicamento.consultar_disponibilidad():
            print(f"Cliente {self.nombre_cliente} solicitó {cantidad} unidades de {medicamento.nombre}.")
            medicamento.actualizar_stock(conexion, -cantidad)
        else:
            print(f"El medicamento {medicamento.nombre} no está disponible en stock.")

    def mostrar_informacion(self):
        print(f"ID Cliente: {self.id_cliente}, Nombre: {self.nombre_cliente}, Teléfono: {self.telefono}, Dirección: {self.direccion}")


# Ejemplo de uso
conexion = conectar_db()

proveedor1 = Proveedor(1, "Laboratorio X", "123456789", "Calle Falsa 123")
proveedor1.guardar_en_db(conexion)

medicamento1 = Medicamento(1, "Amoxicilina", 76.00, 10, proveedor1.id_proveedor)
medicamento1.guardar_en_db(conexion)

cliente1 = Cliente(1, "Juan Perez", "987654321", "Avenida Siempreviva 456")
cliente1.guardar_en_db(conexion)

empleado1 = Empleado(1, "Ana Gomez", "456789123")
empleado1.guardar_en_db(conexion)

# Proceso de venta
cliente1.solicitar_medicamento(conexion, medicamento1, 2)
empleado1.procesar_venta(conexion, cliente1, [(medicamento1, 2)])

conexion.close()