import mysql.connector
import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
from clase_empleado import Empleado
from clasemedicamento import Antibiotico, Antiinflamatorio
from clasecliente import Cliente

# Conexión a la base de datos
def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='bd_sistema_farmacos_controlados'
        )
        return conexion
    except mysql.connector.Error as err:
        messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {err}")
        return None


empleado1 = None
cliente1 = None
medicamentos_disponibles = []
medicamentos_seleccionados = []

# Función para registrar empleado en Tkinter
def registrar_empleado_gui():
    global empleado1
    nombre = simpledialog.askstring("Registrar Empleado", "Ingrese el nombre del empleado:")
    telefono = simpledialog.askstring("Registrar Empleado", "Ingrese el teléfono del empleado:")
    id_empleado = simpledialog.askinteger("Registrar Empleado", "Ingrese el ID del empleado:")
    empleado1 = Empleado(id_empleado, nombre, telefono)
    empleado1.registrar_empleado()
    messagebox.showinfo("Registro Exitoso", f"Empleado {nombre} registrado con éxito.")

# Función para registrar cliente a través de Tkinter
def registrar_cliente_gui():
    global cliente1
    nombre = simpledialog.askstring("Registrar Cliente", "Ingrese el nombre del cliente:")
    telefono = simpledialog.askstring("Registrar Cliente", "Ingrese el teléfono del cliente:")
    direccion = simpledialog.askstring("Registrar Cliente", "Ingrese la dirección del cliente:")
    id_cliente = simpledialog.askinteger("Registrar Cliente", "Ingrese el ID del cliente:")
    cliente1 = Cliente(id_cliente, nombre, telefono, direccion)
    messagebox.showinfo("Cliente Registrado", f"Cliente {nombre} registrado con éxito.")

# Función para manejar la compra de medicamentos
def comprar_medicamentos():
    if not cliente1:
        messagebox.showwarning("Cliente no registrado", "Por favor, registre un cliente antes de realizar la compra.")
        return
    
    total = sum(med.precio for med in medicamentos_seleccionados)
    resultado = f"Empleado: {empleado1.nombre}\nCliente: {cliente1.nombre}\n\nMedicamentos Comprados:\n"
    for med in medicamentos_seleccionados:
        resultado += f"{med.nombre} - ${med.precio}\n"
    resultado += f"\nTotal: ${total:.2f}"
    messagebox.showinfo("Compra Realizada", resultado)
    medicamentos_seleccionados.clear()
    lista_productos.delete(0, tk.END)
    label_total.config(text="0.00")

# Función para seleccionar un medicamento en ktinter
def seleccionar_medicamento():
    medicamento_seleccionado = combobox_medicamentos.get()
    for med in medicamentos_disponibles:
        if med.nombre == medicamento_seleccionado:
            medicamentos_seleccionados.append(med)
            detalle_medicamento = f"{med.nombre} agregado al carrito.\n"
            detalle_medicamento += f"Precio: ${med.precio}\nStock: {med.stock}\n"

            if isinstance(med, Antibiotico):
                detalle_medicamento += f"Concentración: {med.concentracion_en_ml} ml"
            elif isinstance(med, Antiinflamatorio):
                detalle_medicamento += f"Concentración: {med.concentracion_en_mg} mg"

            messagebox.showinfo("Medicamento Agregado", detalle_medicamento)
            calcular_total(med.precio)
            lista_productos.insert(tk.END, f"{med.nombre} - ${med.precio}")
            return
    messagebox.showwarning("Medicamento No Encontrado", f"El medicamento {medicamento_seleccionado} no está disponible.")

# Función para calcular el total de la venta
def calcular_total(precio):
    total = float(label_total.cget("text"))
    total += precio
    label_total.config(text=f"{total:.2f}")

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de Venta de Fármacos Controlados")
root.geometry('1800x1800')

# Crear los menús en la interfaz de Tkinter
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

empleado_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Empleado", menu=empleado_menu)
empleado_menu.add_command(label="Registrar Empleado", command=registrar_empleado_gui)

cliente_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Cliente", menu=cliente_menu)
cliente_menu.add_command(label="Registrar Cliente", command=registrar_cliente_gui)

venta_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Venta", menu=venta_menu)
venta_menu.add_command(label="Seleccionar Medicamento", command=seleccionar_medicamento)
venta_menu.add_command(label="Procesar Venta", command=comprar_medicamentos)

# Información del empleado
label_venta = tk.Label(root, width=50, font=("Times New Roman", 20), text="Sistema de Ventas de Fármacos Controlados")
label_venta.pack(pady=10)

# Crear Combobox para seleccionar medicamentos
label_medicamento = tk.Label(root, width=50, font=("Times New Roman", 18), text="Medicamentos disponibles:")
label_medicamento.pack(pady=10)

combobox_medicamentos = ttk.Combobox(root,width=50, font=("Times New Roman", 18), state="readonly")
combobox_medicamentos.pack(pady=10)

# Información de medicamentos seleccionados 
label_medicamento_disp = tk.Label(root, width=50, font=("Times New Roman", 18), text="Lista de medicamentos:")
label_medicamento_disp.pack()

# Lista de productos
lista_productos = tk.Listbox(root)
lista_productos.pack(pady=10)

# Mostrar el total de la compra
label_total_text = tk.Label(root,width=50, font=("Times New Roman", 18),text="Total:")
label_total_text.pack()

label_total = tk.Label(root,width=50, font=("Times New Roman", 18), text="0.00")
label_total.pack()

# Iniciar datos
def iniciar_datos():
    global medicamentos_disponibles

    medicamento1 = Antibiotico(1, "Amoxicilina", 76.00, 10, '5ml')
    medicamento2 = Antiinflamatorio(2, "Ibuprofeno", 80.00, 13, '600mg')
    medicamentos_disponibles = [medicamento1, medicamento2]

    combobox_medicamentos['values'] = [med.nombre for med in medicamentos_disponibles]
    combobox_medicamentos.current(0)

iniciar_datos()

# Mostrar empleados registrados
def mostrar_empleados():
    if empleado1:
        info_empleado = f"Nombre: {empleado1.nombre}, ID: {empleado1.id_empleado}, Teléfono: {empleado1.telefono}"
        messagebox.showinfo("Empleado Registrado", info_empleado)
    else:
        messagebox.showinfo("Empleado Registrado", "No hay empleados registrados.")

# Mostrar clientes registrados
def mostrar_clientes():
    if cliente1:
        info_cliente = f"Nombre: {cliente1.nombre}, ID: {cliente1.id_cliente}, Teléfono: {cliente1.telefono}, Dirección: {cliente1.direccion}"
        messagebox.showinfo("Cliente Registrado", info_cliente)
    else:
        messagebox.showinfo("Cliente Registrado", "No hay clientes registrados.")

# Botón para ver empleados registrados
boton_mostrar_empleados = tk.Button(root, width=50, font=("Times New Roman", 18), text="Ver datos completos del Empleado Registrado", command=mostrar_empleados)
boton_mostrar_empleados.pack(pady=10)

# Botón para ver clientes registrados
boton_mostrar_clientes = tk.Button(root,width=50, font=("Times New Roman", 18), text="Ver datos completos del Cliente Registrado", command=mostrar_clientes)
boton_mostrar_clientes.pack(pady=10)

# Ejecutar la aplicación Tkinter
root.mainloop()