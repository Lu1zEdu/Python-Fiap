
print('Inicio do Programa')
nome = str(input('Qual o nome do Aluno : \n'))
for i in range (3):
    n = float(input(f'Digite a {i + 1} nota : \n'))
    list.append(n)
media = list[0] + list[1] + list[2] / 3
print(f'A media do {nome} : ' , media)

soma =0
for i  in range (5):
    number = list[i]
    soma = soma + number
    print('Numero :' ,'\tSoma: ', soma )


