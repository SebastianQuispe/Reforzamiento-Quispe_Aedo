class Circulo:
    def __init__(self,radio):
        self.radio=radio
        self.area= pow(self.radio,2)
        self.perimetro= 2*self.radio

circulo1= Circulo(14)
print("El area del circulo es: {} π".format(circulo1.area))
circulo2= Circulo(15)
print("El area del circulo es: {} π".format(circulo2.area))
