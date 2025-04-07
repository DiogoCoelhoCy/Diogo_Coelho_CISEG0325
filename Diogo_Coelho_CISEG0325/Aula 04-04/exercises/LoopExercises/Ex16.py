
pares=[]

for i in range(30):
    par=int(input("Introduza um numero par (1 a 50): "))
    if par > 50 or par < 1:
        print("Valor Incorreto")
        break
    elif par % 2 != 0:
        print("Valor Incorreto")
        break
    elif par % 2 == 0:
        pares.append(par)
    else:
        print("Valor Incorreto")


media=sum(pares)/len(pares)

print(f"A media é {media}")