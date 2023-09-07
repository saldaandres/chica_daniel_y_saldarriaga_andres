# Chica Arboleda Daniel Felipe
# Saldarriaga Ruiz Andres Felipe

lista_carros = ["Mazda CX"]
continuar = "1"

while continuar == "1":
    opcion = input("Escoja una de las opciones.\n1. Eliminar un carro\n2. Actualizar\n3. Consultar\n4. "
                   "Agregar\nDigite su eleccion aqui: ")
    print()

    if opcion == "1":
        referencia = input("Digite la referencia del carro que quiere borrar: ")

        if referencia in lista_carros:
            lista_carros.remove(referencia)
            print(f"Has borrado el carro {referencia}")

        else:
            print(f"La referencia {referencia} no existe")
            print()

    if opcion == "2":
        referencia_vieja = input("Digite la referencia del carro que quiere actualizar: ")
        referencia_nueva = input("Digite la nueva referencia del carro: ")

        if referencia_vieja in lista_carros:
            for i in range(len(lista_carros)):
                if lista_carros[i] == referencia_vieja:
                    lista_carros[i] = referencia_nueva
                    print(f"En la posicion {i} has actualizado el valor a {referencia_nueva}")
                    print()
                    break

        else:
            print("Esta referencia aún no existe")
            print()

    if opcion == "3":
        referencia = input("Digite la referencia del carro que quiere consultar: ")

        if referencia in lista_carros:
            posicion = lista_carros.index(referencia)
            print(f"La referencia {referencia} esta en la posicion {posicion}")

        else:
            print("Esta referencia aún no existe")
            print()

    if opcion == "4":
        referencia = input("Digite la referencia que quiere agregar: ")

        if referencia in lista_carros:
            print("No puedes repetir una referencia que ya existe")
            print()
        else:
            lista_carros.append(referencia)
            print(f"Has agregado el carro {referencia} en la posicion {len(lista_carros) - 1}")
            print()

    continuar = input("Si quieres continuar digita 1. Para salir digita cualquier otra tecla: ")
    print()

print(lista_carros)
