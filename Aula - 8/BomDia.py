print("Progrma para dar bom dia : ")

executar = True

while executar == True:
    print("Digite seu nome :")
    nome = input()
    print("Bom Dia" , nome)

    print("Voce deseja continuar (Sim / Não)")
    continuar = input()

    if continuar == 'Não':
        executar= False
        print("Fim do Programa")
    