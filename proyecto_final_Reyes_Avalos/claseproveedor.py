#clae proveedor 

class Proveedor:
    def __init__(self, id_proveedor, nombre, telefono, direccion):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion

    def mostrar_informacion(self):
        print(f"ID: {self.id_proveedor}, Nombre: {self.nombre}, Teléfono: {self.telefono}, Dirección: {self.direccion}")

    def actualizar_stock(self):
        print(f"Actualizando stock del proveedor {self.nombre}")

    def suministrar_medicamento(self):
        print(f"Suministrando medicamento del proveedor {self.nombre}")