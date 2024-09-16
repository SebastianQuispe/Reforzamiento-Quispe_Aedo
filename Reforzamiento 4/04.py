class Alumno:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = int(nota)

    def imprimir_datos(self):
        datos= Alumno(self.nombre, self.edad, self.nota)
        print(datos.nombre, datos.edad, datos.nota)

    def imprimir_mensaje(self):
        if self.nota >= 11:
            estado="Aprobado"
            print(estado)
        else:
            estado="Desaprobado"
            print(estado)

alumno1= Alumno("Sebastian", 21, 16)
alumno2= Alumno("Zebas", 21, 9)

alumno1.imprimir_datos()
alumno1.imprimir_mensaje()
alumno2.imprimir_datos()
alumno2.imprimir_mensaje()

