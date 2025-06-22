def contar_usuarios():
    cantidad = input("¿Cuántos usuarios desea ingresar?: ")
    if not cantidad.isdigit():
        print("Número inválido.")
        return

    cantidad = int(cantidad)
    mayores = 0
    menores = 0

    for i in range(cantidad):
        print(f"Usuario {i+1}")
        edad = int(input("Edad: "))
        if edad >= 18:
            mayores += 1
        else:
            menores += 1

    print(f"Usuarios mayores de edad: {mayores}")
    print(f"Usuarios menores de edad: {menores}")

contar_usuarios()
