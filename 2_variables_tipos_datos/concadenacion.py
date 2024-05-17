#Concatenar cadenas de caracteres con contenido de variables

nombre="Dagoberto Fiscal"
especialidad="Area de Desarrollo de SW Multiplataforma"
carrera="Ingeniero en Gestión y Desarrollo de SW"

#1er forma de concatenar
print("Mi nombre es: "+nombre+" estoy en la especialidad de: "+especialidad+", en la carrera de: "+carrera)

print("\n")

#segunda forma de concatenar
print("Mi nombre es: ",nombre," estoy en la especialidad de: ",especialidad,", en la carrera de: ",carrera)

print("\n")

#tercera forma de concatenar 
print(f"Mi nombre es:{nombre} estoy en la especialidad de: {especialidad}, en la carrera de: {carrera}")

print("\n")

#cuarta forma de concatenar
print("Mi nombre es:{} estoy en la especialidad de: {}, en la carrera de: {}".format(nombre,especialidad,carrera))

print("\n")

#quinta forma de concatenar
print('Mi nombre es: '+nombre+' estoy en la especialidad de: '+especialidad+', en la carrera de: '+carrera)

print("\n")
