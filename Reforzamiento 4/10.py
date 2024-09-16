class Soldado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pos_x = 0
        self.pos_y = 0
        self.historial = []

    def caminar_x(self, pasos):
        self.pos_x += pasos
        self.historial.append("Caminar X: {} pasos. Nueva posición: ({}, {})".format(pasos,self.pos_x,self.pos_y))

    def caminar_y(self, pasos):
        if self.pos_y + pasos < 0:
            self.pos_y = 0
        else:
            self.pos_y += pasos
        self.historial.append("Caminar Y: {} pasos. Nueva posición: ({}, {})".format(pasos,self.pos_x,self.pos_y))

    def mostrar_historial(self):
        print("Historial de movimientos de {}:".format(self.nombre))
        for movimiento in self.historial:
            print(movimiento)

soldado1 = Soldado("Soldado1")

soldado1.caminar_x(5)
soldado1.caminar_y(3)
soldado1.caminar_x(-2)
soldado1.caminar_y(-4)

soldado1.mostrar_historial()
