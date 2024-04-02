print("Progrma para calcular a Tabuada: ")

print("\n --------------------------------------------- \n")
Escolha =True
while Escolha:
    print("Informe o numero para a tabuada : ")
    n = float(input())
    
    print("\n Iremos variar a tabuada de 0 a 10 \n")

    if n == 0 :
        print("Erro , numero = {n}")
    
    print("Informe o numero para quantidade de numeros para tabuada: ")
    x = float(input())
    for x in range(1 , x):
        a = x * n 
        print(f"{n} x {x:} = {a}")
        

        print("Voce deseja continuar (Sim / Não)")
        novamente = input()
        if novamente == 'Não':
           Escolha =False 
        print("Fim do Programa")