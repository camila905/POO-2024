#Una funcion es un conjunto de instrucciones agrupadas bajo un nombre en particular como un 
#programa mas paqueño que comple una fucion especifica 
#la funcion puede reutilizar con el simple hecho de invorcarla es decir mandarla a llmar.


#Funcion que no recibe parametros y no valor 

def sumaNumeros2():
   n1=int(input("Numero # 1:"))
   n2=int(input("Numero # 2:"))
   suma=n1+n2
   return (f"{n1}+{n2}={suma}")

print(sumaNumeros2(34,23))      


#Funcion que no recibe parametros y no regresa valor 

def sumaNumeros3(n1,n2):
   n1=int(input("Numero # 1:"))
   n2=int(input("Numero # 2:"))
   suma=n1+n2
   return (f"{n1}+{n2}={suma}")

n1=int(input("Numero # 1:")) 
n2=int(input("Numero # 2:"))
sumaNumeros3(n1,n2)


#Funcion que no recibe parametros y no regresa valor 

def sumaNumeros3(n1,n2):
   n1=int(input("Numero # 1:"))
   n2=int(input("Numero # 2:"))
   suma=n1+n2
   return (f"{n1}+{n2}={suma}")

n1=int(input("Numero # 1:")) 
n2=int(input("Numero # 2:"))
print(sumaNumeros3(n1,n2))

#Ejemplo 6 crear un programa que solicite a travez de una funcion la siguente 
#informacion: Nombre del paciente, edad, estatura, tipo de sangre, utilizar los cuatro tipos de funcioones 