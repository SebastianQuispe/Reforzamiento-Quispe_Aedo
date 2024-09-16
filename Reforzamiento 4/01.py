class Persona:

    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.edad = ""
    def pedir_nombre_apellido(self):
        self.nombre = input("Ingrese su nombre: ")
        self.apellido=input("Ingrese su apellido: ")
    def pedir_edad(self):
        self.edad = input("Ingrese su edad: ")

    def imprimir(self):
        datos={
            "nombre":self.nombre,
            "apellido":self.apellido,
            "edad":self.edad
        }
        print(datos)
persona=Persona()
persona.pedir_nombre_apellido()
persona.pedir_edad()
persona.imprimir()
