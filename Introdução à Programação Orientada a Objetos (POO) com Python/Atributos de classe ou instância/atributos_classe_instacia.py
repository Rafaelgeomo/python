class Estudante:
   escola = "DIO"

   def __init__(self, nome, numero):
      self.nome = nome
      self.numero = numero

   def __str__(self) -> str:
      return f" {self.nome} - {self.numero} - {self.escola}"
   
def mostrar_valores(*objs):
   for obj in objs:
      print(obj)
   
aluno_1 = Estudante("Guilherme", 15678)
aluno_2 = Estudante("Giovana", 98676)
mostrar_valores(aluno_1, aluno_2)
aluno_1.numero = 158
mostrar_valores(aluno_1, aluno_2)