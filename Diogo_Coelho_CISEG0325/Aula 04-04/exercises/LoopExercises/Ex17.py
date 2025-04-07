print("Múltiplos de 5 que não são múltiplos de 3 (de 1 a 1000):\n")

for i in range(1, 1001):
    if i % 5 == 0 and i % 3 != 0:
        print(i)

print("\nFim da sequência.")