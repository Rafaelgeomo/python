class Passaro:
   def voar(self):
      print("Voando...")

class Pardal(Passaro):
   def voar(self):
      return super().voar()
   
class Avestruz(Passaro):
   def voar(self):
      print("Avestruz não pode voar")



def plano_voo(obj):
   obj.voar()

p1 = Pardal()

plano_voo(p1) # pode declarar assim e chamar apenas a variavel ou como o exemplo abaixo
plano_voo(Avestruz())