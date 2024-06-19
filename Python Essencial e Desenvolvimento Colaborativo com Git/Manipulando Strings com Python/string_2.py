nome = "Rafael"
idade = 34
profissao = "Programador"
linguagem = "Python"
saldo = 45.435

dados = {"nome":"Rafael", "idade": 34} #dicionario

print("Nome: %s idade: %d" % (nome, idade)) #método old style
print("Nome: {} idade: {}".format (nome, idade)) #método format
print("Nome: {1} idade: {0}".format (idade, nome)) #método format com indice
print("Nome: {nome} idade: {idade}".format (**dados)) #método format com dicionario
print(f"Nome: {nome} idade: {idade}") #método f strings
print(f"Nome: {nome} idade: {idade} Saldo: {saldo:.1f}" ) #método f strings com formatação, o primeiro numero é o espaçamento e o segundo é o numero de casa decimais