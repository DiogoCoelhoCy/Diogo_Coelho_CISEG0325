
print("Bem vindo ao Gestor de notas")


nota1=int(input("Escreva a primeira nota: "))
nota2=int(input("Escreva a segunda nota: "))
nota3=int(input("Escreva a terceira nota: "))

TotalProvas=((nota1*2)+(nota2*3)+(nota3*5))
NotaFinal=TotalProvas/10


if NotaFinal>6:
    print(NotaFinal)
    print("Parabéns voce foi aprovado")
else:
    print(NotaFinal)
    print("Infelizmente voce foi reprovado")
