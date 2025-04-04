print("bem vindo ao BES")

saldo=float(input("Escreva seu saldo da conta: "))
print("")
cheque=float(input("Escreva o valor da cheque: "))

if saldo > cheque:
     saldofinal=saldo-cheque
     print(f"O cheque foi descontado. O seu saldo atual é {saldofinal}")
if saldo < cheque:
     print("Infelizmente o cheque não pode ser descontado por fundos insuficentes.")