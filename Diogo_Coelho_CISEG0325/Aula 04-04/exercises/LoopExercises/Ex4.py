
valor=int(input('Digite um valor: '))


if valor <= 1:
    print(f"{valor} não é um número primo.")
else:
    primo = True
    for i in range(2, int(valor**0.5) + 1):
        if valor % i == 0:
            primo = False
            break
    if primo:
        print(f"{valor} é um número primo.")
    else:
        print(f"{valor} não é um número primo.")