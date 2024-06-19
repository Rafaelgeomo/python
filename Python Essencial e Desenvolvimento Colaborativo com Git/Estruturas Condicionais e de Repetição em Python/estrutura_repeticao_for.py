texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# Exemplo utilizando um iterável
for letras in texto:
  if letras.upper() in VOGAIS:
    print(letras, end="")

print() #adiciona uma quebra de linha

# Exemplo utilizando a função bult-in range
for numero in range(0, 31, 3): # 0 é o start, 31 é o stop, e o 3 é o step
  print(numero, end=" ")