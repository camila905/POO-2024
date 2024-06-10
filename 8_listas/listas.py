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
#i=0
#while i<len(numeros):
    #print(numeros[i])
    #i+=1

#ejemplo 2 crear un lista de palabras posteriormente ingresar un aplabra para buscar la concidencia en la lista si parece 
#e indicar si aparece la palabra y en que posicion en caso contrario indicar un sola vez si no la encuentro 

#palabras=["hola","2024","10.23","True"]

#palabra_busca=input("ingresar la palabra a buscar: ")


#palabras=["hola","2024","10.23","True"]

#palabra_buscar=input("Ingresar la pañabra a buscaar: ")
#noencontro=True 
    #for i in palabras:
    #   if palabra_buscar==i:
    #     print(f"Econtre la palabra {palabra_buscar}, en la posicion: {palabras.index(i)})

#i=0

#eJEMPLO 3 CREAR UNA LISTA MULTILINEA O MULTIDIMENCIONAL (MATRIZ) PARA CREAR UNA AGENDA TELEFONICA 

AGENDA=[
 ["Carlos",6181234567]
 ["Fernado",6182234557]
 ["Matias",6691112233]
 ["Juan Polainas"]
 
     

#ejemplo 4 crear un programa que permita gestionar 
#(administrar) peliculas, colocar un menu de opciones para agregar, remover, consultar peliculas 
#Notas:
#1.- Utilizar funciones y mandar desde otro archivo 
#2.-Utilizar listas para almacenar los libros de peliculas 

   def insertar():


def insetarPeliculas():
   pelicula=input("Ingresar la pelicula: ")
   peliculas.apped(pelicula)
   espereTecla()

   peliculas=[]


print("\n\t..::CINEPOLIS CLON ::...\n 1.-Agregar  \n 2.- Eliminar \n 3.-Consultar \n 4.-Salir")
opcion=input("\t Elige una opcion: ").upper()

if opcion=="1" or opcion=="AGREGAR":
   insertarPeliculas()
elif opcion=="2" or opcion=="ELIMINAR":
   EliminarPeliculas()

def eliminarPeliculas():
   pelicula=input("Ingresar la pelicula: ")
   pelicula.remove(pelicula)
   espereTecla()