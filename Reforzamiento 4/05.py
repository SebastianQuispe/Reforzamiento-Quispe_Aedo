from datetime import datetime


class Persona:
    def __init__(self, nombre, edad, sueldo,fecha_inicio):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
        self.fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
    def datos (self):
        if self.edad >= 18:
            print("Es mayor de edad")
            print(self.nombre,self.edad,self.sueldo,self.fecha_inicio)
        else:
            print("Es menor de edad")
            print(self.nombre, self.edad, self.sueldo, self.fecha_inicio)
    def bonificacion(self):
        if self.edad >= 18:
            return self.sueldo * 0.20
        else:
            return 0

    def meses_trabajando(self):
        fecha_actual = datetime.now()
        diferencia = fecha_actual - self.fecha_inicio
        return diferencia.days // 30

persona_1= Persona("Sebastian",21,500,"2022-01-15")
persona_2= Persona("Juan",17,500,"2023-03-22")

for persona in (persona_1, persona_2):
    persona.datos()
    bonificacion = persona.bonificacion()
    meses = persona.meses_trabajando()
    print("Bonificación: {}".format(bonificacion))
    print("Meses en la empresa: {} meses".format(meses))
    print()
