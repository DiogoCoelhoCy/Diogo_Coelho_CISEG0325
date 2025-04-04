

num = int(input("Digite um número inteiro: "))

contador = 0

print(f"Divisores de {num}: ", end="")

for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
        contador += 1

print(f"\nO número {num} possui {contador} divisores.")