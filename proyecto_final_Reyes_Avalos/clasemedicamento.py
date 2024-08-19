#clase medicamento 

class Medicamento:
    def __init__(self, id_medicamento, nombre, precio, stock):
        self.id_medicamento = id_medicamento
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def actualizar_stock(self, cantidad):
        self.stock += cantidad
        print(f"Nuevo stock de {self.nombre}: {self.stock}")

    def consultar_disponibilidad(self):
        return self.stock > 0

    def mostrar_informacion(self):
        print(f"ID Medicamento: {self.id_medicamento}, Nombre: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}")


class Antibiotico(Medicamento):
    def __init__(self, id_medicamento, nombre, precio, stock, concentracion_en_ml):
        super().__init__(id_medicamento, nombre, precio, stock)
        self.concentracion_en_ml = concentracion_en_ml

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Concentración en ml: {self.concentracion_en_ml}")


class Antiinflamatorio(Medicamento):
    def __init__(self, id_medicamento, nombre, precio, stock, concentracion_en_mg):
        super().__init__(id_medicamento, nombre, precio, stock)
        self.concentracion_en_mg = concentracion_en_mg

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Concentración en mg: {self.concentracion_en_mg}")
        
               
def iniciar_datos():
    global medicamentos_disponibles

    medicamento1 = Antibiotico(1, "Amoxicilina", 76.00, 10, '5ml')
    medicamento2 = Antiinflamatorio(2, "Ibuprofeno", 80.00, 13, '600mg')
    medicamentos_disponibles = [medicamento1, medicamento2]

    # combobox_medicamentos['values'] = [med.nombre for med in medicamentos_disponibles]
    # combobox_medicamentos.current(0)
