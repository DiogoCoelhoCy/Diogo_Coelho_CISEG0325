notas=[]

for i in range(10):
    nota=int(input("Digite um valor: "))
    notas.append(nota)

media=sum(notas)/len(notas)

print(f"A media é: {media}")

