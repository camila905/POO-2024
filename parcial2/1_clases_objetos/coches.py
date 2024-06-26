"""  
 Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.
"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
    marca="Ferrari"
    color="rojo"
    modelo="2010"
    velocidad=300
    caballaje=500
    plazas=2

    #Metodos o acciones o funciones que hace el objeto 

    def acelerar(self):
        self.velocidad+=1

    def frenar(self):
        self.velocidad-=1   

#Fin definir clase

#Crear un objetos o instanciar la clase

coche1=Coches()

#Mostrar los valores inicales del objeto o instancia de la clase
print(f"Marca: {coche1.marca} {coche1.color}, numeros de plazas: {coche1.plazas} \nModelo: {coche1.modelo} con una velocidad de {coche1.velocidad} Km/h y un potencia de {coche1.caballaje} hp")

#Acelerar la velocidad del coche de 300 a 301
coche1.acelerar()
print(f"La nueva velocidad es: {coche1.velocidad}")

#Disminuir la velocidad del coche de 301 a 100

for i in range(1,202):
   coche1.frenar()

print(f"La nueva velocidad del coche es: {coche1.velocidad}")   

 #Crear los metodos setters y getters .- estos metodos son importantes y necesarios en todos clases para que el programador interactue con los valores de los atributos a traves de estos metodos ... digamos que es la manera mas adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a traves de un objeto. 
    # En teoria se deberia de crear un metodo Getters y Setters por cada atributo que contenga la clase
    #   Los metodos get siempre regresan valor es decir el valor de la propiedad a traves del return
    #Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion

    def getColor(self):
      return self.color

    def setColor(self,color):
      self.color=color 

    def getMarca(self):
      return self.marca

    def setMarca(self,marca):
      self.marca=marca 

    def getModelo(self):
      return self.modelo

    def setModelo(self,modelo):
      self.modelo=modelo        

    def getVelocidad(self):
       return self.velocidad

    def setVelocidad(self,velocidad):
      self.velocidad=velocidad 

    def getCaballaje(self):
       return self.caballaje

    def setCaballaje(self,caballaje):
      self.caballaje=caballaje  

    def getPlazas(self):
       return self.plazas

    def setPlazas(self,plazas):
      self.plazas=plazas 

    def getInfo(self):
       print(f"Marca: {self.getMarca()} {self.getColor()}, numeros de plazas: {self.getPlazas()} \nModelo: {self.getModelo()} con una velocidad de {self.getVelocidad()} Km/h y un potencia de {self.getCaballaje()} hp")  

#Fin definir clase coches

#Clases Secundarias, SubClases, Hijas
class Camiones(Coches):
   def __init__(self,color,marca,modelo,velocidad,caballaje,plazas,eje,capacidadCarga):
    super().__init__(color,marca,modelo,velocidad,caballaje,plazas)
    self.eje=eje
    self.capacidadCarga=capacidadCarga

   __tipo_carga=""

   def cargar(self,tipo_carga):
    self.__tipo_carga=tipo_carga
    return self.__tipo_carga

   def getEje(self):
     return self.eje

   def setEje(self,eje):
      self.eje=eje  

   def getcapacidadCarga(self):
     return self.capacidadCarga

   def setcapacidadCarga(self,capacidadCarga):
      self.capacidadCarga=capacidadCarga 

   def getInfo(self):
      print(f"Marca: {self.getMarca()} {self.getColor()}, numeros de plazas: {self.getPlazas()} \nModelo: {self.getModelo()} con una velocidad de {self.getVelocidad()} Km/h, una potencia de {self.getCaballaje()} hp, con {self.getEje()} ejes y una capacidad de carga de {self.getcapacidadCarga()} metros cubicos")       


class Camionetas(Coches):
  def __init__(self,color,marca,modelo,velocidad,caballaje,plazas,trasera,cerrada):
    super().__init__(color,marca,modelo,velocidad,caballaje,plazas)
    self.traccion=trasera
    self.cerrada=cerrada

  __num_pasajeros=0
  def transportar(self,num_pasajeros):
      self.__num_pasajeros=num_pasajeros
      return self.__num_pasajeros

  def setTraccion(self,traccion):
     self.traccion=traccion

  def getTraccion(self):
    return self.traccion

  def setCerrada(self,traccion):
     self.cerrada=cerrada

  def getCerrada(self):
    return self.cerrada

  def getInfo(self):
      print(f"Marca: {self.getMarca()} {self.getColor()}, numeros de plazas: {self.getPlazas()} \nModelo: {self.getModelo()} con una velocidad de {self.getVelocidad()} Km/h, una potencia de {self.getCaballaje()} hp, con la tracción {self.getTraccion()} y es cerrada {self.getCerrada()} ")  




