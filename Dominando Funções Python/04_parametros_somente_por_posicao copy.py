def criar_carro(modelo, ano, placa, /, marca, motor, combustivel): #colocando a barra tudo q vem antes precisa ser declarado por posição 
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #maneira correta
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # maneira errada, dará invalido
