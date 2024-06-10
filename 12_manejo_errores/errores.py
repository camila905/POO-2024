#Manejo de errores es la forlma en la que tiene los lenguajes de errrores de programaciacion para evitar que 
#sucedan eerores en tiemppo de ejecucion 

#Ejemplo 1 erroro cuando una variable no se genera 

try:
    nombre=int(input("Dame el nombre: "))

if len(nombre)>1:
    nombre_usuario="El nombre es: "+nombre

print(nombre_usuario)
except:
print("Es necesario introducir un nombre de usuario...")

#Ejemplo cuando se solicita un numero y se introduce un letra 

numero=int(input("dAme un numero: "))

if numero>0:
   print("Soy un numero entero positivo")
else:
   print("Soy un numero entero negativo")
except:
print("No se puede convertit un caracter no numerico a numero a numero...")

#Ejemplo cuando se solicita un numero y se introduce letra 
try:
    numero=int(input("Dame un numeo: "))
    if numero>0:
     print("Soy un numero entero positivo")
    else:
       print("Soy un numero entero negativo")
except:
   print("No se puede convertit un caracter no nuerico a nuero...")
else:
   print("Todo se ejecuto sin errores")

#Ejemplo numero 3 cuando se generan multiples excepciones

try:
   numero=int)input("Dame un numero: ")

print("El cuadrado es: "+str(numero*numero))
except valueError:
print("Debes de introducir un numro no se puede convertit un caracter que no sea numerico")
except:
print("No es posble convertir el numero a entero")
else:
