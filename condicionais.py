# if, elif e else

idade = int(input("Qual é a sua idade?"))

if idade >= 18:
  print("Você é maior de idade.")
elif idade >= 12:
  print("Você é um adolescente")
else:
  print("Você é menor de idade.")


mensagem = "Pode tirar a carteira de motorista" if idade >= 18 else "Você não \
tem idade suficiente para tirar a carteira e motorista."

print(mensagem)