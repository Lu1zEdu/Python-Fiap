print(" Iremos calcular a media dos alunos \n")

Escolha = True
while Escolha :
    print("Nome do aluno :")
    nome = input()

    print("nota do aluno na prova 1 :")
    cp1 = float(input())
    print("nota do aluno na prova 2 :")
    cp2 = float(input())
    print("nota do aluno na prova 3 :")
    cp3 = float(input())

    Media = cp1 + cp2 + cp3 / 3

    print("\nNome          Nota 1    Nota 2     Nota 3    Media ")
    print(f"{nome:<12} {cp1:<9.1f}{cp2:<9.1f}{cp3:<9.1f}{Media:>5.1f}\n")

    #print(" {nome} tem a media :{Media}")

    print("Voce deseja continuar (Sim / Não)")
    novamente = input()
    if novamente == 'Não':
        Escolha = False
    print("Fim do Programa")
