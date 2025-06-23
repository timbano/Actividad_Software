# archivo3.py
# 3. Verificar si una palabra es palíndromo
palabra = input("Ingrese una palabra: ").lower()
if palabra == palabra[::-1]:
    print("Es palíndromo")
else:
    print("No es palíndromo")
