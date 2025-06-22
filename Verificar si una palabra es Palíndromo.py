def es_palindromo():
    palabra = input("Ingrese una palabra: ").replace(" ", "").lower()
    if palabra == palabra[::-1]:
        print("Es un palíndromo.")
    else:
        print("No es un palíndromo.")

es_palindromo()
