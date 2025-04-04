
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
    print(f"{num1} é o maior.")
elif num2>num1 and num2>num3:
    print(f"{num2} é o maior")
else:
    print(f"{num3} é o maior")

#MENOR
if num1<num2 and num1<num3:
    print(f"{num1} é o menor.")
elif num2<num1 and num2<num3:
    print(f"{num2} é o menor")
else:
    print(f"{num3} é o menor")