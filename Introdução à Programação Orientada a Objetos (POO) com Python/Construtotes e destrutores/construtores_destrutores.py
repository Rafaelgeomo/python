class Cachorro:
   def __init__(self, nome, cor, acordado=True):
      print("Inicializando a class...")
      self.nome = nome
      self.cor = cor
      self.acordado = acordado

   def __del__(self):
      print("Removendo a instância da class")

   def falar(self):
      print("auau")


def criar_cachorro():
   c = Cachorro ("Zeus", "Branco", False)
   print(c.nome)


# c = Cachorro("Mustafah", "Branco e Marrom")
# c.falar()

criar_cachorro()