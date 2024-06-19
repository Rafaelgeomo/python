contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.keys()  # dict_keys(['guilherme@gmail.com'])
print(resultado)

# keys retorna so a chave do dicionario, que no caso seria "guilherme@gmail.com"

#exemplo

novo_dicionario = {"nome": "Rafael", "idade": 34, "cachorro": "Mustafah"}
print(novo_dicionario.keys()) #retornou apenas, nome, idade, cachorro, que são as chaves do dicionario