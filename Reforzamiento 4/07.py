class Agenda:
    def __init__(self):
        self.contactos = []

    def añadir_contacto(self, nombre, telefono, email, dni):
        contacto = {
            'nombre': nombre,
            'telefono': telefono,
            'email': email,
            'dni': dni
        }
        self.contactos.append(contacto)
        print("Contacto {} añadido con éxito.".format(nombre))

    def mostrar_contactos(self):
        if not self.contactos:
            print("No hay contactos en la agenda.")
            return
        for contacto in self.contactos:
            print("Nombre: {} ".format(contacto['nombre']))
            print("Teléfono: {} ".format(contacto['telefono']))
            print("Email: {} ".format(contacto['email']))
            print("DNI: {} ".format(contacto['dni']))
            print()

    def buscar_contacto_por_dni(self, dni):
        for contacto in self.contactos:
            if contacto['dni'] == dni:
                print("Nombre: {}".format(contacto['nombre']))
                print("Teléfono: {}".format(contacto['telefono']))
                print("Email: {}".format(contacto['email']))
                print("DNI: {}".format(contacto['dni']))
                return
            else:
                print("No se encontró ningún contacto con DNI {}.".format(dni))

agenda=Agenda()
agenda.añadir_contacto("Sebastian Quispe", "971-722-739", "sebas@example.com", "75119512")
agenda.añadir_contacto("Raton Perez", "987-654-321", "raton@example.com", "87654321B")
agenda.añadir_contacto("Marta Martinez", "555-666-777", "marta@example.com", "23456789C")
agenda.añadir_contacto("Lorenzo Matorrales", "444-555-666", "lorezno@example.com", "34567890D")

print("Lista de contactos en la agenda:")
agenda.mostrar_contactos()
print("Buscando contacto con DNI 75119512: ")
agenda.buscar_contacto_por_dni("75119512")