print("Bem vindo")

notas=[]

for i in range (10):
    nota=int(input(f"Escreva a nota do aluno {i + 1} (0 a 20): "))
    notas.append(nota)

media=sum(notas)/len(notas)

notasacima=[]
notasabaixo=[]

for i in notas:
    if i>media:
        notasacima.append(i)
    if i<media:
        notasabaixo.append(i)


print(f"A media das notas é: {media:.2f}")
print(f"As seguintes notas ficaram acima: {notasacima}")
print(f"As seguintes notas ficaram abaixo: {notasabaixo}")