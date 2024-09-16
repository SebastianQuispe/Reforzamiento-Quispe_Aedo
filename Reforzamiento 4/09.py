import math

class Figura:
    def __init__(self, nombre):
        self.nombre=nombre

    def area_rectangulo(self,base ,altura):
        return base*altura

    def perimetro_rectangulo(self,base, altura):
        return (base + altura)* 2

    def radio(self,radio):
        return pow(radio,2) * math.pi

    def area_circulo(self, radio):
        area=self.radio(radio)
        print("Area del circulo es: {}".format(area))

figura1=Figura("figura1")
print("Nombre de la figura: {}".format(figura1.nombre))

base_rectangulo = float(input("Ingrese la base del rectángulo: "))
altura_rectangulo = float(input("Ingrese la altura del rectángulo: "))
print("Area del rectangulo: {}".format(figura1.area_rectangulo(base_rectangulo,altura_rectangulo)))
print("Perimetro del rectangulo: {}".format(figura1.perimetro_rectangulo(base_rectangulo,altura_rectangulo)))

figura2=Figura("figura2")
print("Nombre de la figura: {}".format(figura2.nombre))

base_rectangulo = float(input("Ingresa la base del rectangulo: "))
altura_rectangulo = float(input("Ingresa la altura del rectangulo: "))
print("Area del rectangulo: {}".format(figura2.area_rectangulo(base_rectangulo,altura_rectangulo)))
print("Perimetro del rectangulo: {}".format(figura2.perimetro_rectangulo(base_rectangulo,altura_rectangulo)))

figura3=Figura("circulo")
print("Nombre de la figura: {}".format(figura3.nombre))
radio = float(input("Ingresa el radio del circulo: "))
figura1.area_circulo(radio)

