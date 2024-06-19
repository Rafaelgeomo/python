# exibir o programa no terminal python -i nome do arquivo

#VARIAVEIS ------------------------------------------------------------------------
nome = 'Rafael' # Pode declarar variavel em duas linhas ou na mesma linha conforme exemplo abaixo.
idade = 34

#print (nome, idade)

nome, idade = 'Rafael Jeronymo', 35

print (nome,idade)

limite_saque_diario = 1000 #snake case

#print(limite_saque_diario)

BRAZILIAN_STATES = ["SP", "RJ", "SC", "BA"] #Padrão universal para usar como constantes já que o python nao existe constantes.

#print(BRAZILIAN_STATES)

#CONVERTENDO TIPOS --------------------------------------------------------------------------------------

#print(int(1.9)) #Convertendo para um numero float para numero inteiro
#print(int("10")) #Convertendo uma string para numero inteiro
#print(float("10.10")) #Convertendo uma string para numero float
#print(float(100)) #Convertendo para um numero inteiro para numero float
#print(100 / 2) #Divide e converte para um numero float
#print(100 // 2) #Divide e converte para um numero inteiro 
#print(str(10.10)) #Convertendo para um numero inteiro para numero string

#PRINT INPUT --------------------------------------------------------------------

nome_input = input("Informe o seu nome: ")
idade_input = input("Informe a sua idade: ")
print(nome_input, idade_input)
print(nome_input, idade_input, end=" ...\n")
print(nome_input, idade_input, sep="_")
