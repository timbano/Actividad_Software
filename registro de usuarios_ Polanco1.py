def registrar_usuario():
    nombre = input("Nombre: ")
    correo = input("Correo electrónico: ")
    edad = input("Edad: ")

    if not edad.isdigit():
        print("Edad inválida.")
        return

    edad = int(edad)

    if "@" not in correo or not correo.endswith(".com"):
        print("Correo inválido.")
        return

    if edad < 18:
        print("Debe tener al menos 18 años.")
        return

    print("Registro exitoso.")
    print(f"Nombre: {nombre}, Correo: {correo}, Edad: {edad}")

registrar_usuario()
