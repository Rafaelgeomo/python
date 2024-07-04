def mensagem(nome):
   print("executando nome")
   return f"Oi {nome}"

def mensagem_longa(nome):
   print("executando mensagem longa")
   return f"Olá tudo bem com você {nome}?"

def executar(funcao, nome):
   print("executando o executar")
   return funcao(nome)

print(executar(mensagem,"Rafael"))
print(executar(mensagem_longa,"Rafael"))