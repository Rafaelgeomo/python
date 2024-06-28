from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
   @abstractmethod
   def ligar(self):
      pass
   
   @abstractmethod
   def desligar(self):
      pass
   
   @property
   @abstractproperty
   def marca(self):
      pass

class ControleTV(ControleRemoto):
   def ligar(self):
      print("Ligando a TV")
      print("TV Ligada!")

   def desligar(self):
      print("Desligando a TV")
      print("TV desligada!")

   @property
   def marca(self):
      return "LG"

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)