print("Progrma para calcular a area de retangulos : ")

print("\n --------------------------------------------- \n")

while True:
    print("Informe a Base em metros de seu Retangulo :")
    base = float(input())
    print("Informe a Altura em metros de seu Retangulo :")
    
    altura = float(input())
    
    area = base * altura
    print(f"O tamanho da area é : {area} cm2")
    print("Fim do Progrma")

    print("Voce deseja continuar (Sim / Não)")
    novamente = input()
    if novamente == 'Não':
        break

    # break serve para quebrar o laço (While)

print("Fim do Programa")