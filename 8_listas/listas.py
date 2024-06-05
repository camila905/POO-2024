#List(Array)
#son colleciones o conjunto de datos/valores bajo un mismo nombre para acceder a los valores se hace con un indice numerico 
#Nota: sus valores si son modificlables 
#Las} lista es una colleccion ordenada y modificable permite miembros duplicados

#EJEMPLO 1 CREAR UNA LSITA CON VALORES NUMERICOS ENTEROS ES IMPRIMIR LISTA 

numero=23
nummero=34

numeros=[23,34]
print(numeros)

#recorres la lista con un for 

for i in numeros:
    print(i)

#recorre la lista con un while
i=0
while i<len(numeros):
    print(numeros[i])
    i+=1

#ejemplo 2 crear un lista de palabras posteriormente ingresar un aplabra para buscar la concidencia en la lista si parece 
#e indicar si aparece la palabra y en que posicion en caso contrario indicar un sola vez si no la encuentro 

palabras=["hola","2024","10.23","True"]

palabra_busca=input("ingresar la palabra a buscar: ")


palabras=["hola","2024","10.23","True"]

palabra_buscar=input("Ingresar la pañabra a buscaar: ")

for i in palabras:
    if palabra_buscar==i:
        print(f"Encontre la palabra {palabra_buscar}, e la posicion: {palabras.index(i)}")
        noencontro=False

    noencontro:
    print(f"No se encontro la palabra dentro de la lista")

    palabras_buscar=input("Ingresar la palabra a buscar: ")

    noencontro=True 
    #for i in palabras:
    #   if palabra_buscar==i:
    #     print(f"Econtre la palabra {palabra_buscar}, en la posicion: {palabras.index(i)})