nome = "Matheus"
nome.upper()  # Maiúscula
nome.lower()  # Minuscula 

#       0123456
nome = "Matheus"
nome[0]

# Quantas vezes a ocorrência está escrita
nome_completo = "Gabriel Casemiro"
nome.count("a")

# Vai achar o índice da ocorrência deseja
#                0123456
nome_completo = "Gabriel Casemiro"
print(nome.find("a")) 

# Vai converter a string, para bytes
nome_completo = "Gabriel Casemiro"
nome.encode() 

# Vai desconverter a byte, para string
nome_completo = "Gabriel Casemiro"
nome.encode() 
nome.encode().decode() 

# Faz a substituição de um para outro.
telefone = "(11) 94258-3609"
print(telefone.replace(" ", "").replace("(", "").replace(")", "").replace("-", ""))

# Join separa a string com a ocorrência desejada
print("~". join(nome))

# Converte a string em um Array com indices, separa partir da ocorrência desejada.
print(nome_completo.split(" "))

# Remove caracteres das extremidades de uma string com ruídos.
nome_ruido = "xGabriel Casemirox"
print(nome_ruido.strip("x"))

# Remove caracteres da direita de uma string com ruídos.
print(nome_ruido.rstrip("x")) 

# Começa com, procura as primeiras ocorrências, retornando boolean
print(nome_completo.startswith("Gabriel"))

# in existe? return boolean 
print("Ga" in nome_completo)


# not in não existe! return boolean
print("Filipe" not in nome )