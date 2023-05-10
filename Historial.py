# Desarrollar un programa que permita gestionar el historial clínico de pacientes en una clínica. El programa deberá utilizar dos clases: Paciente y Historial.

# La clase Paciente deberá tener los siguientes atributos:
# nombre: el nombre del paciente.
# edad: la edad del paciente.
# género: el género del paciente.
# historial: un objeto de la clase Historial que contiene la información médica del paciente.
# La clase Paciente deberá tener los siguientes métodos:

# agregar_historial(sintomas, diagnostico, tratamiento): agrega una entrada al historial del paciente con la información médica especificada.
# mostrar_historial(): muestra por pantalla todas las entradas del historial del paciente.
# La clase Historial deberá tener los siguientes atributos:

# entradas: una lista de diccionarios, donde cada diccionario representa una entrada del historial clínico del paciente y contiene la información médica de la misma.
# La clase Historial deberá tener los siguientes métodos:

# agregar_entrada(sintomas, diagnostico, tratamiento): agrega una nueva entrada al historial con la información médica especificada.
# mostrar_entradas(): muestra por pantalla todas las entradas del historial clínico.
# El programa deberá permitir al usuario realizar las siguientes acciones:

# Agregar un nuevo paciente, ingresando su nombre, edad y género.
# Agregar una nueva entrada al historial clínico de un paciente, ingresando su nombre, sintomas, diagnóstico y tratamiento.
# Mostrar el historial clínico de un paciente.
# Mostrar todas las entradas del historial clínico de todos los pacientes.
# El programa deberá mostrar un menú al usuario con las diferentes opciones, y permitirle elegir la opción deseada ingresando un número.

class Historial:
    def __init__(self):
        self.historial =[]
    def agregar(self, sintomas, diagnostico, tratamiento):
        entrada={
            "sintomas":sintomas,
            "diagnostico":diagnostico,
            "tratamiento":tratamiento
        }
        self.historial.append(entrada)

    def mostrar(self):
        for elemento in self.historial:
            print('----Historia Clinica----')
            print('Sintomas: ',elemento['sintomas'])
            print('Diagnostico: ',elemento['diagnostico'])
            print('Tratamiento: ',elemento['tratamiento'])


h1 = Historial()
h1.agregar("Dolor de Cabeza","Gripe Fuerte","Antigripales")
h1.mostrar()

