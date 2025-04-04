
num=[]

for i in range(10):
    valor=int(input('Digite um valor: '))
    num.append(valor)

for j in num:
    if j % 2 == 0:
        print(f"Par: {j}")
    else:
        print(f"Impar: {j}")
