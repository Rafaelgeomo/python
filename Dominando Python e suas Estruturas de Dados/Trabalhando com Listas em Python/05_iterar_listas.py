carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros): #enumerate mostra o indice que se encontra cada item da lista
    print(f"{indice}: {carro}")
