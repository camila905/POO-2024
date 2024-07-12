class Personas:
    def __init__(self, Nombre, Edad, Tel):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Tel = Tel

    def getNombre(self):
        return self.Nombre

    def setNombre(self, Nombre):
        self.Nombre = Nombre

    def getEdad(self):
        return self.Edad

    def setEdad(self, Edad):
        self.Edad = Edad

    def getTel(self):
        return self.Tel

    def setTel(self, Tel):
        self.Tel = Tel

    def getInfo(self):
        print(f"Nombre: {self.Nombre}, Edad: {self.Edad}, Numero de Tel: {self.Tel}")







        
