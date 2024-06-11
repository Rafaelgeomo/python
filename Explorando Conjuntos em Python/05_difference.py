conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.difference(conjunto_b) #pega o que é diferente do conjunto a que nao tem no conjunto b, que seria o numero 1
print(resultado)

resultado = conjunto_b.difference(conjunto_a) # nesse caso pego o que tem diferente no b que nao tem no a, seria o numero 4
print(resultado)
