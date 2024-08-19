#clase factura 

class Factura:
    def __init__(self, id_factura, numero_factura, fecha_emision):
        self.id_factura = id_factura
        self.numero_factura = numero_factura
        self.fecha_emision = fecha_emision

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