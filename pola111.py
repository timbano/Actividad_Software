# archivo2.py
# 2. Calcular el factorial de un número
n = int(input("Ingrese un número: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("El factorial es", factorial)
