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

class Empleado(Persona):
    def apto_para_prestamo(self):
        meses_trabajando = self.meses_trabajando()
        if meses_trabajando > 12 and self.edad > 25:
            return True
        else:
            return False
    def prestamo(self):
        if self.apto_para_prestamo():
            return self.sueldo*10
        else:
            return 0

empleado1=Empleado("Juan",25,500,"2022-01-15")
empleado2=Empleado("Ignacio",30,500,"2023-03-22")
empleado3=Empleado("Pedro",18,500,"2021-05-10")

for empleado in (empleado1, empleado2, empleado3):
    empleado.datos()
    apto = empleado.apto_para_prestamo()
    monto = empleado.prestamo()
    if apto:
        print("El empleado es apto para un prestamo de: {}".format(monto))
    else:
        print("El empleado no es apto para un prestamo")
    print()

