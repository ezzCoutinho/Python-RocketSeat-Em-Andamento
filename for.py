lista = [1, 2, 3, 4, 5]
print("Lista")
for elemento in lista:
  print(elemento)

tupla = (1, 2, 3, 4, 5)
print("Tupla")
for elemento in tupla:
  print(elemento)

pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

print("\n---APENAS AS CHAVES---")
for chave in pessoa.keys():
  print(chave)
print("\n---APENAS VALORES---")
for valor in pessoa.values():
  print(valor)
print("\n---CHAVES E VALORES---")
for chave, valor in pessoa.items():
  print(f"{chave}: {valor}")