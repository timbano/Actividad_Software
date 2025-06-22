def area_perimetro():
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    area = base * altura
    perimetro = 2 * (base + altura)
    print(f"Área: {area}")
    print(f"Perímetro: {perimetro}")

area_perimetro()
