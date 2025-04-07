
a, b = 1, 1
contador = 2

print("Primeiros 60 números da sequência de Bonatchi (Fibonacci):\n")
print(a, b, end=' ')

while contador < 60:
    proximo = a + b
    print(proximo, end=' ')
    a, b = b, proximo
    contador += 1

print("\n\nFim da sequência.")
