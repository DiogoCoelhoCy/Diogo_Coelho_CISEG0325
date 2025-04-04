print("Bem vindo")

notas=[]

for i in range (11):
    nota=int(input(f"Digite a nota do aluno {i + 1} (0 a 20): "))
    notas.append(nota)

media=sum(notas)/len(notas)

for i in notas:
    if i>media:
        j=i
    if i<media:
        q=i


print(f"A media das notas é: {media:.2f}")
print(f"As seguintes notas ficaram acima: {j}")
print(f"As seguintes notas ficaram abaixo: {q}")
