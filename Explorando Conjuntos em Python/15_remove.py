numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.remove(0))  # 0, diferente do discard ele da um erro se pedir para remover um item que nao existe
print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
