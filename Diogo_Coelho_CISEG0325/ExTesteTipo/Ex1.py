

def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def divisores(n):
    return len([i for i in range(1, n + 1) if n % i == 0])


def perfeito(n):
    soma = sum(i for i in range(1, n) if n % i == 0)
    return soma == n


def parimpar(n):
    return "Par" if n % 2 == 0 else "Ímpar"


def vernumeros():
    valores = []
    contador=0

    while len(valores) < 50:
        insertval=int(input(f"\nDigite um valor {len(valores) + 1}: "))

        if 1 < insertval < 1000:
            valores.append(insertval)
            contador += 1

            print(f"Valor inserido: {insertval}")
            print(f"o valor é primo: {primo(insertval)}")
            print(f"O valor tem {divisores(insertval)} divisores")
            print(f"O valor é perfeito: {perfeito(insertval)}")
            print(f"O valor é {parimpar(insertval)}")

            if contador % 10 == 0 and len(valores) <= 50:
                sair=input("Sair do programa? (s/n) ").lower()
                match sair:
                    case "s":
                        print("Saindo...")
                        break
                    case "n":
                        continue
                    case _:
                        print("Opção invalida.")
    return valores



def calculadora():
    global sub, div, mul, adi
    while True:
        print("\n--- Calculadora ---")
        print("1. Adição")
        print("2. Subtração")
        print("3. divisão")
        print("4. Multiplicação")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adi=[]
            for i in range(5):
                insertadi=int(input("Digite um valor: "))
                if 1 < insertadi < 1000:
                    adi.append(insertadi)
                else:
                    print("Valor fora do intervalo permitido (1 a 999).")

            soma=sum(adi)
            print(f"A soma dos elementos dá {soma}")

            continuar=input("\nPretende sair (s/n)?").lower()
            match continuar:
                case "n":
                    continue
                case "s":
                    break
                case _:
                    print("Opção inválida.")
                    continue

        elif opcao == "2":
            sub=[]
            for i in range(5):
                insertsub=int(input("Digite um valor: "))
                if 1 < insertsub < 1000:
                    sub.append(insertsub)
                else:
                    print("Valor fora do intervalo permitido (1 a 999).")

            resultado_subtracao = sub[0]
            for ele in range(1,len(sub)):
                resultado_subtracao -= sub[ele]
            print(f"O resultado da subtração sequencial é: {sub}")

            continuar=input("\nPretende sair (s/n)?").lower()
            match continuar:
                case "n":
                    continue
                case "s":
                    break
                case _:
                    print("Opção inválida.")
                    continue

        elif opcao == "3":
            div=[]
            for i in range(5):
                insertdiv=float(input("Digite um valor: "))
                if 1 < insertdiv < 1000:
                    div.append(insertdiv)
                else:
                    print("Valor fora do intervalo permitido (1 a 999).")

            resultado_divisao = div[0]
            for ele in range(1,len(div)):
                resultado_divisao /= div[ele]
            print(f"O resultado da divisão sequencial é: {div}")

            continuar=input("\nPretende sair (s/n)?").lower()
            match continuar:
                case "n":
                    continue
                case "s":
                    break
                case _:
                    print("Opção inválida.")
                    continue

        elif opcao == "4":
            mul=[]
            for i in range(5):
                insertmul=float(input("Digite um valor: "))
                if 1 < insertmul < 1000:
                    mul.append(insertmul)
                else:
                    print("Valor fora do intervalo permitido (1 a 999).")

            resultado_multiplicacao = mul[0]
            for ele in range(1,len(mul)):
                resultado_multiplicacao *= mul[ele]
            print(f"O resultado da mulltiplicação sequencial é: {mul}")

            continuar=input("\nPretende sair (s/n)?").lower()
            match continuar:
                case "n":
                    continue
                case "s":
                    break
                case _:
                    print("Opção inválida.")
                    continue





while True:
    print("\n--- MENU ---")
    print("1. Ver números")
    print("2. Calculadora")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        vernumeros()

    elif opcao == "2":
        calculadora()

    elif opcao == "3":
        break








