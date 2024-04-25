def menu_principal():
    print("SISTEMA DE GESTÃO PARA HORTIFRUTI")
    print("MENU PRINCIPAL")
    print("(C)adastrar um produto")
    print("(L)istar os produtos")
    print("(S)air do sistema")


def solicita_opcao():
    print("Escolha sua opcao: ")
    return input().lower()[0]


def produto_cadastrar( lista_produto ):
    produto = {}
    print("Digite o nome do produto: ")
    produto["nome"] = input()
    print("Digite a cor do produto: ")
    produto["cor"] = input()
    print("Digite o preço do produto: ")
    produto["preco"] = float(input())
    print("Digite a unidade de medida do produto: ")
    produto["unidade_medida"] = input()
    lista_produto.append( produto )


def produto_listar( lista_produto ):
    for p in lista_produto:
        print(f"Nome Produto: {p['nome']}\tCor: {p['cor']}")
        print(f"Preço: {p['preco']:.2f}\tUnidade de Medida: {p['unidade_medida']}")
        print("-"*60)



# Trecho do programa principal
lista = []
executando = True 

while executando:
    menu_principal()
    opcao = solicita_opcao()
    if opcao == 'c':
        produto_cadastrar( lista )
    elif opcao == 'l':
        produto_listar( lista )
    elif opcao == 's':
        print("Obrigado por usar o sistema, até breve")
        executando = False

print("Fim do programa")