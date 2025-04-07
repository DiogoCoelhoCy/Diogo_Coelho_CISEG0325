
numero=(int(input('Digite um valor: ')))

soma_total = 0
subtracao_total = numero
multiplicacao_total = 1
divisao_total = numero
operacoes_efetuadas = 0

for i in range(1, numero):
        print(f"\nOperando com {i}:")

        soma = i
        soma_total += soma
        print(f"{numero} + {i} = {numero + i}")
        operacoes_efetuadas += 1

        subtracao = i
        subtracao_resultado = numero - i
        print(f"{numero} - {i} = {subtracao_resultado}")
        operacoes_efetuadas += 1

        multiplicacao = i
        multiplicacao_resultado = numero * i
        print(f"{numero} * {i} = {multiplicacao_resultado}")
        operacoes_efetuadas += 1

        divisao = i
        divisao_resultado = numero / i
        print(f"{numero} / {i} = {divisao_resultado}")
        operacoes_efetuadas += 1


print(f"\nTotal de operações efetuadas: {operacoes_efetuadas}")