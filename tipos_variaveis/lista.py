# Declaração 
minha_lista = [1, 2, 3, 4, 5, "rocketseat", True, False]

# Exibindo a lista
print("Minha lista como exemplo", minha_lista)

# Exibindo índices da lista
minha_lista[0] = "python" # Mutável
print("minha_lista[0], ", minha_lista[0])
print("minha_lista[0], ", minha_lista[5])
print("minha_lista[1:6], ", minha_lista[1:6])
# Do começo até...
print("minha_lista[:3]", minha_lista[:3])
# Do alvo até...
print("minha_lista[8:]", minha_lista[6:])

# Este método faz com oq um valor seja atribuido no final de um Array.
minha_lista.append(6)

# Nos retorna o índice da ocorrência desejada.
indice = minha_lista.index(6)
print(indice)

indice_removido = minha_lista.pop(2)
print("Elemento removido: ", indice_removido)
print(minha_lista)

minha_lista.remove(True)
print(minha_lista)

minha_lista_number = [1, 2, 7, 9, 8, 3, 4, 5, 6]
minha_lista_number.sort()
print(minha_lista_number)