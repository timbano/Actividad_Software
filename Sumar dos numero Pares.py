def sumar_pares():
    cantidad = int(input("¿Cuántos números vas a ingresar?: "))
    suma = 0
    for i in range(cantidad):
        num = int(input(f"Número {i+1}: "))
        if num % 2 == 0:
            suma += num
    print("Suma de pares:", suma)

sumar_pares()
