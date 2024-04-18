print("Progrma para calcular a Tabuada: ")

print("\n --------------------------------------------- \n")

print("Informe o numero para a tabuada : ")
n = int(input())

print("\n --------------------------------------------- \n")

for i in range(0 , 11, 1):
    res = n * i
    print(f"{n} x {i:>2} = {res:>2}")