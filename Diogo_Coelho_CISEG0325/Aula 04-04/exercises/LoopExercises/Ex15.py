import binascii

print("Tabela ASCII (códigos de 0 a 255)\n")

for i in range(0, 256, 20):
    for j in range(i, min(i + 20, 256)):
        try:
            print(f"Código: {j:3} -> Caractere: {chr(j)}")
        except:
            print(f"Código: {j:3} -> Caractere: Não imprimível")