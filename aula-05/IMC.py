print('Por favor informe seu peso : ')
Peso = float(input())
print('Por favor informe sua altura : ')
Altura = float(input())
if Altura < 0:
    print('Altura aceitavel')
else :
    if Altura >400:
        print('altura esta errada')
'''if Altura <0 or Altura > 400
     print('Altura esta errada')   '''
IMC = Peso / (Altura**2)
if IMC > 25:
    print('Você precisa emagrecer')
else :
    print('Você não precisa emagrecer ')
print(IMC)
print('Fim do Programa')