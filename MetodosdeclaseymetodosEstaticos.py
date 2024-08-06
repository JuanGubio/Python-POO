class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

class Estudiante(Persona):
    total_estudiantes = 0

    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
        Estudiante.total_estudiantes += 1
    
    def presentar(self):
        return f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y estudio {self.carrera}."
    
    @classmethod
    def contar_estudiantes(cls):
        return f"Total de estudiantes: {cls.total_estudiantes}"

    @staticmethod
    def info_escuela():
        return "La escuela ofrece una variedad de carreras en ciencia y tecnología."

# Crear instancias de la clase Estudiante
estudiante1 = Estudiante("Ana", 20, "Ingeniería")
estudiante2 = Estudiante("Luis", 22, "Matemáticas")

# Llamar al método de clase contar_estudiantes
print(Estudiante.contar_estudiantes())

# Llamar al método estático info_escuela
print(Estudiante.info_escuela())
