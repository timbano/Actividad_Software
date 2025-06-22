def calcular_promedio():
    nombre = input("Nombre del estudiante: ")
    notas = []

    for i in range(3):
        try:
            nota = float(input(f"Ingrese la nota {i+1}: "))
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("La nota debe estar entre 0 y 10.")
                return
        except ValueError:
            print("Entrada inválida.")
            return

    promedio = sum(notas) / len(notas)
    print(f"{nombre} tiene un promedio de {promedio:.2f}")

    if promedio >= 7:
        print("Estado: Aprobado")
    else:
        print("Estado: Reprobado")

calcular_promedio()
