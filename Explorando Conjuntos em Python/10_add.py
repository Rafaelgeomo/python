sorteio = {1, 23}

sorteio.add(25)  # {1, 23, 25}, adiciona o elmento se ele nao existir
print(sorteio)

sorteio.add(42)  # {1, 23, 25, 42}
print(sorteio)

sorteio.add(25)  # {1, 23, 25, 42}, se existir ele ignora 
print(sorteio)
