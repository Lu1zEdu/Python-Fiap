print('')
for i in range (12):
    altura = float(input(f'Qual a alutra da sua planta no meses {i +1} : \n'))
    list.append(altura)
media = (list[0] + list[1] + list[2] + list[3] + list[4] + list[5] + list[6] + list[7] + list[8] + list[9] ) / 10
print('A media da altura : ' , media)
    
'''-------------------------------'''
print('crescimento anual')

crescimento = []

for i in range (12) :
    print(f'Por favor digite o crescimento do mês {i +1} : ')
    crescimento_mês=float(input())
    crescimento.append(crescimento_mês)
soma = 0
for i in range (12):
    soma = soma +crescimento[i]
media = soma /12
print('Média : ' , media)