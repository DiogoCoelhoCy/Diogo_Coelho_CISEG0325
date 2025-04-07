numero=int(input("Introduza o numero: "))

print(f"Tabuada do {numero}")
for i in range(1, 11):
        multiplicacao = i
        multiplicacao_resultado = numero * i
        print(f"{numero} * {i} = {multiplicacao_resultado}")