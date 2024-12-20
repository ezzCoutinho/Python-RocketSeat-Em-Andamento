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

print(list(range(0,11)))

for numero in range(5):
  print(numero)

lista = [1,2,3,4,5]

for indice in range(0, len(lista)):
  print("Indice:", indice)
  print("Elemento:", lista[indice])
  if indice == 2:
    lista[indice] = 244
  else: 
    lista[indice] = 0
print(lista)

lista_enumerate = ["a", "b", "c"]

for indice, valor in enumerate(lista_enumerate):
  print(f"{indice}: {valor}")
  if valor == "c":
    print("Fim.")