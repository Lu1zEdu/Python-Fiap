e = True
while e == True:
  print("Por favor digite seu nome : ")
  nome = input()
  print(" Bom dia ", nome)
  print("Voce deseja para executar novamente ? (S / N)")
  r = input()
  if r == 'S ':
    e = True
  else:
    e = False
    print("Fim")
