print("Inicio do Programa")
print("Linhas : ")
linhas = int(input())
print("Colunas : ")
colunas = int(input())
for l in range( 0, linhas):
    for c in range ( 0 , colunas):
        print(c + 1, end="")
    print("")

print("\nfim do Programa")