from Historial import Historial
class Paciente:
    def __init__(self,nombre, edad, genero):
        self.nombre=nombre
        self.edad = edad
        self.genero = genero
        self.historial=Historial()

    def agregar_historial(self,sintomas, diagnostico, tratamiento):
        # h1 = Historial(sintomas,diagnostico,tratamiento)
        # self.historial = h1
        self.historial.agregar(sintomas,diagnostico,tratamiento)

    def mostrarHistorial(self):
        print("Lista de Historial clinico del paciente")
        self.historial.mostrar()
    
