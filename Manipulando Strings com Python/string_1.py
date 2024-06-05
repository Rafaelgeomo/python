nome = "RaFaEl"

print(nome.upper()) #deixa todas as letras em maiusculas
print(nome.lower()) #deixa todas as letras em minusculas
print(nome.title()) #deixas apenas a primeira letra em maiuscula


texto = "  Olá mundo!   "

print(texto + ".")
print(texto.strip() + ".") #retira os espaçamentos da direita e da esquerda
print(texto.lstrip() + ".") #retira o espaçamento apenas da esquerda left strip
print(texto.rstrip() + ".") #retira o espaçamento apenas da direita right strip

menu = "Python"

print("####" + menu + "####") #Pode centralizar dessa forma mas nao é indicado
print(menu.center(14, "#")) # Ou pode usar o center e colocar a quantidade de caracter total que vai ter e o que deseja colocar em volta da palavra
print(menu.center(14)) #Não colocando nada como parametro ele apenas alinha ao centro contando a quantidade a mais que vc colocou, ex Pyhton tem 6 caracter entao ficou 4 a mais para direita e 4 para esquerda
print("P-y-t-h-o-n") # para nao precisar usar dessa forma podemos usar o join
print("-".join(menu)) # Ele pega o primeiro parametro que vc colocou e separa a palavra com esse parametro.