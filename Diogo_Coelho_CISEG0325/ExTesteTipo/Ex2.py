

marcas = []
modelos = []

def introduzir_dados():
    if len(marcas) >= 100:
        print("Limite de marcas atingido.")
        return
    marca=input("Insira o nome da marca: ")
    modelo=input("Insira o nome da modelo: ")
    if modelo in modelos:
        print("Modelo já consta na lista")
        return
    marcas.append(marca)
    modelos.append(modelo)
    print("Sucesso!")

def procurar_dados():
    busca = input("\nInsira o nome da marca ou modelo que deseja procurar: ").lower()
    encontrados = False
    for i in range(len(marcas)):
        if busca in marcas[i].lower() or busca in modelos[i].lower():
            print(f"Posição {i}: Marca: {marcas[i]}, modelo: {modelos[i]}")
            encontrados = True
    if not encontrados:
        print("Nenhum marca ou modelo existe")

def eliminar_dados():
    try:
        apagar = int(input("\nInsere o nr do carro a ser removido: "))
        if 0 <= apagar <= len(marcas):
            print("Apagando...")
            del marcas[apagar]
            del modelos[apagar]
            print("Sucesso!")
        else:
            print("Posição não existe")
    except ValueError:
        print("Insira um numero valido")


while True:
    print("\n--- MENU ---")
    print("1. Introduzir Dados")
    print("2. Procurar Dados")
    print("3. Eliminar Dados")
    print("4. Mostrar todos os carros\n")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        introduzir_dados()

    elif opcao == "2":
        procurar_dados()

    elif opcao == "3":
        eliminar_dados()

    elif opcao == "4":
        for i in range(len(marcas)):
            print(f"{i}: Marca: {marcas[i]}, Modelo: {modelos[i]}")
    else:
        print("\nOpção invalida!")