from Paciente import *

pacientes = []
while True:
    print('--------------------------------------')
    print('----     GESTION DE PACIENTES     ----')
    print('--------------------------------------')
    
    print('1. Agregar un nuevo Paciente')
    print('2. Agregar una nueva entrada al historial clinico de un paciente')
    print('3. Mostrar el historial clinico de un paciente')
    print('4. Mostrar todas las entradas del historial clinico de todos los pacientes')
    print('5. Salir')
    opcion = int(input('Ingrese la Opcion: '))
    if opcion ==1:
        nombre = input('Ingrese el nombre: ')
        edad= int(input('Ingrese la edad: '))
        sexo= input('Ingrese el sexo: ')
        p1 = Paciente(nombre,edad,sexo)
        pacientes.append(p1)
    elif opcion==2:
        i =0
        for x in pacientes:
            print(i+1,' ',x.nombre)
            i+=1  
        nombr= input('Ingrese el nombre del paciente: ')
        for y in pacientes:
            if y.nombre  == nombr:
               print('Paciente: ', y.nombre)
               sintoma = input('Ingrese el sintoma: ')
               diagnostico =input('Ingrese el diagnostico: ')
               tratamiento =input('Ingrese el tratamiento: ')
               y.agregar_historial(sintoma,diagnostico,tratamiento)
                  
    elif opcion==3:
        i =0
        for y in pacientes:
            print(i,' ',y.nombre)
            i+=1
        nombr= input('Ingrese el nombre del paciente: ')
        for y in pacientes:
            if y.nombre  == nombr:
                print('Paciente: ', y.nombre)
                y.historial.mostrar()
            i+=1
    elif opcion==4:
        i =0
        for x in pacientes:
            print(i,' ',x.nombre)
            x.historial.mostrar()
            i+=1
    elif opcion == 5: 
        break   