

print("Bem vindo" "\nConversor de segundos")
print("")

valor=int(input("Diga-me o numero de segundos que pretende converter: "))

horas=(valor/3600)
resto=valor%3600
minutos=(resto%3600/60)
segundos=(resto%60)

print(f"O total de segundos dá: {horas:.0f}h :{minutos:.0f}m :{segundos:.0f}s")