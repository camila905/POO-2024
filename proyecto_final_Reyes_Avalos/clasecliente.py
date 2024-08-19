#clase cliente
class Cliente:
    def __init__(self, id_cliente, nombre, telefono, direccion):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion

    def mostrar_informacion(self):
        print(f"ID: {self.id_cliente}, Nombre: {self.nombre}, Teléfono: {self.telefono}, Dirección: {self.direccion}")

    def realizar_pedido(self, medicamentos_disponibles, empleado):
        medicamentos_a_comprar = []
        total_medicamentos = int(input("¿Cuántos tipos de medicamentos diferentes deseas comprar? "))

        for _ in range(total_medicamentos):
            print("\nMedicamentos disponibles:")
            for idx, med in enumerate(medicamentos_disponibles):
                print(f"{idx + 1}. {med.nombre} - Precio: {med.precio} - Stock: {med.stock}")

            seleccion = int(input("Selecciona el número del medicamento que deseas comprar: ")) - 1

            if seleccion < 0 or seleccion >= len(medicamentos_disponibles):
                print("Selección inválida. Intenta nuevamente.")
                continue

            cantidad = int(input(f"¿Cuántas unidades de {medicamentos_disponibles[seleccion].nombre} deseas comprar? "))

            if cantidad > medicamentos_disponibles[seleccion].stock:
                print(f"No hay suficiente stock de {medicamentos_disponibles[seleccion].nombre}.")
            else:
                medicamento = medicamentos_disponibles[seleccion]
                medicamentos_disponibles[seleccion].stock -= cantidad
                medicamentos_a_comprar.append((medicamento, cantidad))

        if medicamentos_a_comprar:
            empleado.procesar_venta(medicamentos_a_comprar)


def comprar_medicamentos(medicamentos_disponibles, empleado):
    cliente1 = Cliente(1, "Jose", "+6183566830", "jose@gmail.com")
    cliente1.realizar_pedido(medicamentos_disponibles, empleado)

class Cliente:
    def __init__(self, id_cliente, nombre, telefono, direccion):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion

    def registrar_cliente(self):
        conexion = conectar_bd()
        if conexion:
            try:
                cursor = conexion.cursor()
                sql = "INSERT INTO clientes (id_cliente, nombre, telefono, direccion) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (self.id_cliente, self.nombre, self.telefono, self.direccion))
                conexion.commit()
                messagebox.showinfo("Registro Exitoso", f"Cliente {self.nombre} registrado en la base de datos con éxito.")
            except mysql.connector.Error as err:
                messagebox.showerror("Error al Registrar", f"No se pudo registrar el cliente: {err}")
            finally:
                conexion.close()