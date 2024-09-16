class Persona:
    def __init__(self):
        self.nombre = input("Ingrese el nombre: ")
        self.edad = int(input("Ingrese la edad: "))
class Empresa(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = int(input("Ingrese el sueldo: "))

    def calcular_sueldo(self):
        if self.sueldo > 4000:
            impuesto=self.sueldo*0.10
        else:
            impuesto=0
        return impuesto

    def datos(self):
        print("Nombre: ", format(self.nombre))
        print("Edad: ", format(self.edad))
        print("Sueldo: ", format(self.sueldo))
        impuesto = self.calcular_sueldo()
        if impuesto > 0:
            print("Debe pagar de impuesto: {}".format(impuesto))
        else:
            print("No debe pagar impuestos.")

empleado = Empresa()
empleado.datos()