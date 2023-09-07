# Chica Agudelo Daniel Felipe
# Saldarriaga Ruiz Andres Felipe

diccionario_carros = {
    "Mazda CX": 90
}
continuar = "1"

while continuar == "1":
    opcion = input("Escoja una de las opciones.\n1. Eliminar un carro\n2. Actualizar\n3. Consultar\n4. "
                   "Agregar\nDigite su eleccion aqui: ")
    print()

    if opcion == "1":
        referencia = input("Digite la referencia del carro que quiere borrar: ")

        if referencia in diccionario_carros.keys():
            del diccionario_carros[referencia]
            print(f"Has borrado la refencia {referencia}")
            print()
        else:
            print(f"La referencia {referencia} no existe")
            print()

    if opcion == "2":
        referencia = input("Digite la referencia del carro que quiere actualizar: ")

        if referencia in diccionario_carros.keys():
            nuevo_precio = int(input("Digite el nuevo precio del carro: "))
            diccionario_carros.update({referencia: nuevo_precio})
            print(f"Has actualizado la referencia {referencia} con el precio {nuevo_precio}")
            print()
        else:
            print("Esta referencia aún no existe")
            print()

    if opcion == "3":
        referencia = input("Digite la referencia del carro que quiere consultar: ")

        if referencia in diccionario_carros.keys():
            valor = diccionario_carros[referencia]
            print(f"La referencia {referencia} tiene un precio de {valor}")
            print()
        else:
            print("Esta referencia aún no existe")
            print()

    if opcion == "4":
        referencia = input("Digite la referencia que quiere agregar: ")

        if referencia in diccionario_carros.keys():
            print("No puedes repetir una referencia que ya existe")
            print()
        else:
            precio = int(input("Digite el valor del nuevo carro: "))
            diccionario_carros[referencia] = precio
            print(f"Has agregado el carro {referencia} con un precio de {precio}")
            print()

    continuar = input("Si quieres continuar digita 1. Para salir digita cualquier otra tecla: ")
    print()

print(diccionario_carros)


