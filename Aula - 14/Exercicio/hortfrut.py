lista = []
def Heade():
    print("""
          cadastrar produtos da feira
          """)
 
def Menu():
    print("Cadastro == 1")
    print("listar todos os produtos == 2")
    print("pesquisar por um produto == 3")
    print("Sair == 4")
    escolha_menu()

def escolha_menu():
    escolha = input("Qual das opcoes acima : \n ")
    try:
        if escolha == 1:
            Cadastro()
        elif escolha == 2:
            listar()
        elif escolha == 3 :
            pesquisar()
        elif escolha == 4 :
            sair()
        else:
            sair()
    except:
        sair()

def Cadastro():
    numero = int(input('Quantidade de produtos :\n'))
    for i in range(numero):
        dict1 ={}
        nome = input("Qual o nome do produto :\n")
        dict["nome"] = nome
        cor = input("Qual a cor do produto : \n")
        dict["cor"] = cor
        preco = input("Qual o preco do produto :\n")
        dict["preco"] = preco
        unidade_mediada =input("Qual a uniadade de medida do produto :\n")
        dict["unidade_mediada"] = unidade_mediada
        lista.append(dict1)

def listar():
    for p in lista:
        print("Produto : " , p["nome"])
        print("Cor  :" , p["cor"])
        print("Preço : " , p["preco"])
        print("Uniadade De Medida : " , p["unidade_mediada"])

def pesquisar():
    name= input("Qual o nome do produto a se pesquisado :\n")
    for c in lista:
        if name == c['name']:
            print("Produto : " , c["nome"])
            print("Cor  :" , c["cor"])
            print("Preço : " , c["preco"])
            print("Uniadade De Medida : " , c["unidade_mediada"])

def sair():
    print("Sair")

def main():
    Heade()
    Menu()
    escolha_menu()

if __name__ == "__main__":
    main()

'''
produto = {}
produto["nome"] =  input("Qual o nome do produto :\n")
'''