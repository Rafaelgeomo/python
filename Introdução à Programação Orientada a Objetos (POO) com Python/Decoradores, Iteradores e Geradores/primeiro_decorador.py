def meu_decorador(funcao):
   def envelope():
      print("Faz algo antes de executar")
      funcao()
      print("Faz algo depois de executar")

   return envelope

@meu_decorador #colocando esse @ nao precisa passar o meu decorador por referencia, so chamando o ola mundo ja irá funcionar
def ola_mundo():
   print("Olá mundo!")


# ola_mundo = meu_decorador(ola_mundo)
ola_mundo()
