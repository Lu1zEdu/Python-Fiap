s ="Hello Word"
print("Texto : " + s)
s_minusculo = s.lower() #"hello word"
print("Text Minusculo : " + s_minusculo)
#--------------------------------------------------#
s_maiusculo =s.upper()
print("Texto Maiusculo" , s_maiusculo)
#--------------------------------------------------#
tamanho = len(s) #int 13
print("Tamanho da String :" ,tamanho)
print("Tamanho da String :" ,str(tamanho) )
#--------------------------------------------------#
# 012345666666678901234567890123456678901
texto = "A FIAP é uma faculdade bem legal"
tam = len(texto)
print("Tamanho : " , tam)
letra =texto[17]
print("Letra na posiçao 17 : " + letra)
letra =texto[20]
print("Letra na posiçao 20 : " + letra)

pos = texto.find("legal")
print(" O texto possui a palavra legal na posicão : " , pos)

tos = texto.find("FIAP")
print(" O texto possui a palavra FIAP na posicão : " , tos)

vos = texto.find("manhã")
print(" O texto possui a palavra manhã na posicão : " , vos)

mos = texto.find("m")
print(" O texto possui a letra m na posicão : " , mos)

dos = texto.find("m" , 11)
print(" O texto possui a letra m na posicão : " , dos)

oos = texto.find("m" , 26)
print(" O texto possui a letra m na posicão : " , oos)

qos = texto.find("m" , 11)
print(" O texto possui a letra m na posicão : " , qos)

