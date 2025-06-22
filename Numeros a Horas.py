def convertir_minutos():
    total_minutos = int(input("Ingrese minutos: "))
    horas = total_minutos // 60
    minutos = total_minutos % 60
    print(f"{total_minutos} minutos son {horas} horas y {minutos} minutos.")

convertir_minutos()
