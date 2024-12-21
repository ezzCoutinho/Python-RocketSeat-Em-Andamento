# Função.
def saudacao(nome):
  print(f"Ola, {nome}!")

saudacao("Matheus")

# Função com retorno.
def quadrado(numero):
  resultado = numero ** 2
  return resultado

print("\n Chamando a função ao quadrado:")
resultado_quadrado = quadrado(6)
print("Resultado da função quadrado:", resultado_quadrado)

# Função com múltiplos parâmetros.

def soma(x, y):
  soma = x + y
  return print(f"O Resultado da soma é: {soma}")

soma(99, 1)