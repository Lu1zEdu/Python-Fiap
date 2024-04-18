d1 = {
    'aluno' : '40',
    'professor' : 'Antonio' ,
    'computadores' : '43',
    'cadeiras' : '43',
    'monitores' :'43' , 
    'perifericos' :{
        'computadores' : '43',
        'monitores' :'43' 
    }
}
d1['sala_aula'] = 201
if 'sala_aula' in d1:
    print("existe a chave 'sala_aula'  no dicionario ")
else:
    print(" não existe a chave 'sala_aula'  no dicionario ")

print(d1)
for chave in d1.keys():
    print(chave , "=>" , d1[chave])