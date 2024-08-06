   
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
    
    def presentar(self):
        return f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y estudio {self.carrera}."


estudiante1 = Estudiante("Ana", 20, "Ingeniería")


print(estudiante1.presentar())
