
class Circulo:
    def __init__(self,radio):
        self.radio=radio
        self.area= pow(self.radio,2)

radio= float(input("Ingrese el radio del circulo: "))
circulo= Circulo(radio)
print("El are del circulo es: {} π".format(circulo.area))

