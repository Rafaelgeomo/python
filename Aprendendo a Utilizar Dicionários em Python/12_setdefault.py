contato = {"nome": "Guilherme", "telefone": "3333-2221"}

contato.setdefault("nome", "Giovanna")  # "Guilherme", so o atributo nao estiver nao estiver no dicionario ele add com o valor que foi passado, se existir ele retorna o atributo
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("idade", 28)  # 28, nesse exemplo nao existe então será adicionado com o valor de 28.
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}
