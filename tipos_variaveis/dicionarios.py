# Criando um dicionário NÃO ORDENADO, com pares de chave e valor

pessoa = {"nome": "Gabriel", "idade": 30, "cidade": "São Paulo"}

print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

pessoa["sobrenome"] = "Silva"
print("Sobrenome:", pessoa["sobrenome"])

pessoa["idade"] = 31 
print("Idade atualizada:", pessoa["idade"])

del pessoa["sobrenome"]

chaves = list(pessoa.keys())
print("Chaves do dicionário:", chaves)
print(chaves[0])

valor_das_chaves = list(pessoa.values())
print("Todos os valores do dicionário:", valor_das_chaves)
print(valor_das_chaves[0])

itens = list(pessoa.items())
print(itens)
print("Primeira chave-valor da tupla: %s = %s" % (itens[0][0], itens[0][1]))