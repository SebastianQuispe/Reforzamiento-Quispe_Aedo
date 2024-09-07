var1={'nombre': 'Sebastian', 'Salario': 1500, 'DNI': 75119512}
var1_key=list(var1.values())
for elemento in var1_key:
    print("Elemento: {}, Tipo: {}".format(elemento, type(elemento)))