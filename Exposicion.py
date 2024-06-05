class Nodo:
    def __init__(self, decision, resultado=None):
        self.decision = decision
        self.resultado = resultado
        self.hijos = []

    def agregar_hijo(self, nodo):
        self.hijos.append(nodo)

def imprimir_arbol(nodo, nivel=0):
    print('  ' * nivel + str(nodo.decision))
    if nodo.resultado is not None:
        print('  ' * (nivel + 1) + f'Resultado: {nodo.resultado}')
    for hijo in nodo.hijos:
        imprimir_arbol(hijo, nivel + 1)

# Creando el árbol de decisión
raiz = Nodo("¿Llueve?")
llueve = Nodo("Sí", "Mantenerse en casa")
no_llueve = Nodo("No", "Salir de casa")

raiz.agregar_hijo(llueve)
raiz.agregar_hijo(no_llueve)

# Imprimiendo el árbol de decisión
imprimir_arbol(raiz)