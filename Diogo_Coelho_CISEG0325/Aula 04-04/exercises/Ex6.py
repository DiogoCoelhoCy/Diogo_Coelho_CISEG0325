nome=input('Escreva o seu nome: ')

valorcompra=float(input('Digite o valor da sua compra (€): '))

if valorcompra <= 200:
    desconto_percentual=10
elif valorcompra <= 500:
    desconto_percentual=15
else:
    desconto_percentual=20

desconto=(valorcompra*desconto_percentual)/100

valor_final=valorcompra-desconto

print("\n--- Resumo da Compra ---")
print(f"Cliente: {nome}")
print(f"Valor da compra: {valorcompra:.2f}€")
print(f"Percentual de desconto: {desconto_percentual}%")
print(f"Valor do desconto: {desconto:.2f}€")
print(f"Total a pagar: {valor_final:.2f}€")