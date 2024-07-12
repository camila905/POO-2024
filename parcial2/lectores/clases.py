class lectores:
    def _init_(self,Nombre,Tel,Direccion):
        self.Nombre = Nombre
        self.Direccion = Direccion
        self.Tel = Tel

    def reservar(self):
        return self.Nombre

    def setNombre(self, Nombre):
        self.Nombre = Nombre

    def getDireccion(self):
        return self.Direccion

    def setDireccion(self, Direccion):
        self.Direccion = Direccion

    def getTel(self):
        return self.Tel

    def setTel(self, Tel):
        self.Tel = Tel

    def getInfo(self):
        print(f"Nombre: {self.Nombre}, Direccion: {self.Direccion}, Numero de Tel: {self.Tel}")

class Estudiantes(lectores):
   def _init_(self,nombre,direccion,tel,carrera,matricula):
     super()._init_(nombre,direccion,tel)
     self._carrera=carrera
     self._matricula=matricula

   def reservar(self):
        print(f"El estudiante: {self.getNombre()} reservo un libro y su matricula es: {self.getMatricula()} de la carrera de: {self.getCarrera()}")

   def entregar(self):
        print(f"El estudiante: {self.getNombre()} entrego un libro y su matricula es: {self.getMatricula()} de la carrera de: {self.getCarrera()}")

   def getCarrera(self):
      return self._carrera
   def getMatricula(self):
      return self._matricula
   
   def setCarrera(self,carrera):
      self._carrera=carrera
   def setMatricula(self,matricula):
      self._matricula=matricula     

class Docentes(lectores):
   def _init_(self,nombre,direccion,tel,modalidad,num_empleado):
     super()._init_(nombre,direccion,tel)
     self.__modalidad=modalidad
     self.__num_empleado=num_empleado

   def reservar(self):
        print(f"El docente: {self.getNombre()} reservo un libro y su numero de empleado es: {self.getNum_empleado()} de la modalidad de: {self.getModalidad()}")

   def entregar(self):
        print(f"El docente: {self.getNombre()} entrego un libro y su numero de empleado es: {self.getNum_empleado()} de la modalidad de: {self.getModalidad()}")

   def getModalidad(self):
      return self.__modalidad
   def getNum_empleado(self):
      return self.__num_empleado
   
   def setModalidad(self,modalidad):
      self.__modalidad=modalidad
   def setMatricula(self,num_empleado):
      self.__num_empleado=num_empleado

    