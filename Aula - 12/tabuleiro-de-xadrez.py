
'''
    Tabuleiro de Xadrez
'''

Linha1 = ""
caractere = "#"
for x in range(0 , 8):
    for i in range (0,5):
        Linha1 += caractere
    caractere = " " if caractere == "#" else "#"

caractere = " "
Linha2 = ""
for j in range(0 , 8):
    for i in range (0,5):
        Linha2 += caractere
    caractere = " " if caractere == "#" else "#"
    

for i in range (0,4):
    for i in range(0,3):
        print(Linha1)
    for i in range(0,3):
        print(Linha2)