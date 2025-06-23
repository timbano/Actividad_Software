# archivo5.py
# 5. Mostrar los primeros 10 números de la serie Fibonacci
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
