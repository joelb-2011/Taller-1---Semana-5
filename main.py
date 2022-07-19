from datetime import date
import os

class Usuario:
    def __init__(self, nombre, cedula, direccion, numtelf, email):
        self.nombre = nombre
        self.cedula = cedula
        self.direccion = direccion
        self.numtelf = numtelf
        self.email = email
        
class Persona(Usuario):
    def __init__(self, nombre, cedula, direccion, numtelf, email):
        super().__init__(nombre, cedula, direccion, numtelf, email)
    def mostrarEstudiante(self):
        print(f"{self.nombre} {self.cedula} {self.direccion} {self.numtelf} {self.email}")
        
class Administrador(Usuario):
    def __init__(self, nombre, cedula, direccion, numtelf, email):
        super().__init__(nombre, cedula, direccion, numtelf, email)
    def mostrarDocente(self):
        print(f"{self.nombre} {self.cedula} {self.direccion} {self.numtelf} {self.email}")
        
from abc import ABC, abstractclassmethod

class Rol(ABC):
    def __init__(self, nombre, cedula, direccion, numtelf, email):
        super().__init__(nombre, cedula, direccion, numtelf, email)
        
    @abstractclassmethod
    
    def mostrarRol(self):
        print(f"{self.nombre} {self.cedula} {self.direccion} {self.numtelf} {self.email}")
        
class Usuario:
    def __init__(self, nombre, cedula, direccion, numtelf, email):
        self.nombre = nombre
        self.cedula = cedula
        self.direccion = direccion
        self.numtelf = numtelf
        self.email = email
        
class Estudiante(Usuario): 
    def __init__(self, nombre, cedula, direccion, numtelf, email):
        super().__init__(nombre, cedula, direccion, numtelf, email)
    def mostrarEstudiante(self):
        print(f"{self.nombre} {self.cedula} {self.direccion} {self.numtelf} {self.email}")
        
class Docente(Usuario):
    def __init__(self, nombre, cedula, direccion, numtelf, email):
        super().__init__(nombre, cedula, direccion, numtelf, email)
    def mostrarDocente(self):
        print(f"{self.nombre} {self.cedula} {self.direccion} {self.numtelf} {self.email}")
        
class OpcSistema:
    _registro = 0
    def __init__(self, codigo, descripcion, record, nomb, rol, emp, ruc):
        self.codigo = codigo
        self.descripcion = descripcion
        self.consulta = record
        OpcSistema._registro += 1
        self._registro = "#0" + str(OpcSistema._registro)
        self.date = date.today()
        self.nomb = nomb
        self.rol = rol
        self.emp = emp
        self.ruc = ruc
        
    def mostrarOpcSistemaPersona(self):
        print(f"Consulta: {self._registro:14} Empresa: {self.emp:14} Fecha: {self.date}")
        print(f"Nombre: {self.nomb:16} Ruc: {self.ruc:18} Rol: {self.rol}")
        print("=" * 29, "Record crediticio", "=" * 29)
        print("Cedula              Estado        Record crediticio")
        print(f"{self.codigo:14} {self.descripcion:25} {self.consulta}")
    def mostrarOpcSistemaAdministrador(self):
        print()
        print(f"Consulta: {self._registro:20} Empresa: {self.emp:24} Fecha: {self.date}")
        print(f"Nombre: {self.nomb:22} Ruc: {self.ruc:29}Rol: {self.rol}")
        print("=" * 45, "Record crediticio", "=" * 45)
        print("Codigo        Nombre       Record crediticio   Aumentar/disminuir record crediticio   Ultima modificacion")
        print("{:7} {:22} {:30} +{}-                  {} " .format(self.codigo, self.descripcion, self.consulta, OpcSistema._registro, self.date))
        
while True:
    
    print()
    print(" " * 20,"Menu de Inicio"," " * 20)
    print("1. Cliente natural.")
    print("2. Administrador.")
    print("3. Salir.")
    opc= int(input("Ingrese una opción [1...3]: "))
    if opc == 1:
        os.system("cls")
        print(" " * 20,"Opciones del sistema"," " * 20)
        print("1. Consultar buro crediticio. ")
        print("2. Regresar al menu de inicio.")
        print("3. Oprime cualquier tecla para salir.")
        opc2 = input("Ingrese una opcion [1...3]: ")
        if opc2 == '1':
            os.system("cls")
            notas = OpcSistema("0952482148", "Centro de salud", "42", "Joel Barrionuevo", "Cliente natural", "Servicios JB", "0900405047013")
            notas.mostrarOpcSistemaPersona()
            opc3 = input("Oprime cualquier tecla para ir al menu de inicio: ")
            if opc3 == opc3:
                os.system("cls")
            else:
                os.system("cls")
                print("Error. La opción seleccionada es incorrecta.")
        elif opc2 =='2':
            os.system("cls")
        elif opc2 == opc2:
            os.system("cls")
            print("Gracias por usar nuestro sistema.")
            break
        else:
            os.system("cls")
            print("Error. La opción seleccionada es incorrecta.")
    elif opc == 2:
        os.system("cls")
        print(" " * 20,"Opciones del sistema"," " * 20)
        print("1. Consultar buro crediticio. ")
        print("2. Regresar al menu de inicio.")
        print("3. Oprime cualquier tecla para salir.")
        opc4 = input("Seleccione una opcion [1...3]: ")
        if opc4 == '1':
            os.system("cls")
            notas2 = OpcSistema("0952482148","Joel Barrionuevo","42","Sanchez","Administrador","Servicios JB","0900405047013")
            notas2.mostrarOpcSistemaAdministrador()
            print()
            opc5 = input("Seleccione cualquier tecla para regresar al menu principal: ")
            if opc5 == opc5:
                os.system("cls")
            else:
                os.system("cls")
                print("Error. La opción seleccionada es incorrecta.")
        elif opc4 == '2':
            os.system("cls")
        elif opc4 == opc4:
            os.system("cls")
            print("Gracias por usar nuestro sistema.")
            break
        else:
            os.system("cls")
            print("Error. La opción seleccionada es incorrecta.")
    elif opc == 3:
        os.system("cls")
        print("Gracias por usar nuestro sistema.")
        break
    else:
        os.system("cls")
        print("Error. La opción seleccionada es incorrecta.")