#clase ventas

class Ventas:
    def __init__(self, id_ventas, fecha_ventas):
        self.id_ventas = id_ventas
        self.fecha_ventas = fecha_ventas
        self.ventas = []

    def registrar_venta(self, medicamento, cantidad):
        subtotal = medicamento.precio * cantidad
        self.ventas.append({
            'medicamento': medicamento,
            'cantidad': cantidad,
            'subtotal': subtotal
        })

    def generar_factura(self, id_factura, numero_factura):
        factura = Factura(id_factura, numero_factura, self.fecha_ventas)
        return factura