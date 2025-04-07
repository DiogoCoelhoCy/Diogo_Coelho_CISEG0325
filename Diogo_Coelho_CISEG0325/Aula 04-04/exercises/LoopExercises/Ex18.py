limite = int(input("Digite o número limite para verificar números perfeitos: "))
contador= 0

print(f"\nNúmeros perfeitos entre 1 e {limite}:")

for num in range(1, limite + 1):
    soma_divisores = 0

    for i in range(1, num):
        if num % i == 0:
            soma_divisores += i

    if soma_divisores == num:
        print(num)
        contador += 1

print(f"\nTotal de números perfeitos encontrados: {contador}")