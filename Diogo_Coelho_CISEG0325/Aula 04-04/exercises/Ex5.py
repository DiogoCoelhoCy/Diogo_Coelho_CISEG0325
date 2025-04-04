print("Bem vindo")
print("")

num1=0
num2=0
num3=0

num1=int(input("Escreve um nr: "))
num2=int(input("Escreve um nr: "))
num3=int(input("Escreve um nr: "))

#MAIOR
if num1>num2 and num1>num3:
    maior=num1
elif num2>num1 and num2>num3:
    maior=num2
else:
    maior=num3

#MENOR
if num1<num2 and num1<num3:
    menor=num1
elif num2<num1 and num2<num3:
    menor=num2
else:
    menor=num3

meio = (num1 + num2 + num3) - (maior + menor)

print(f"Ordem crescente:  {menor}, {meio}, {maior}")
print(f"Ordem decresente:  {maior}, {meio}, {menor}")