class Veiculo:
   def __init__(self, cor, placa, numero_rodas):
      self.cor = cor
      self.placa = placa
      self.numero_rodas = numero_rodas

   def ligar_motor(self):
      print("Ligando o motor")

   def __str__(self): # Método para exibir a instância por completo com os valores, diferente do método acima qualquer mudança na classe nao precisa mexer aqui.
      return f"{self.__class__.__name__}:{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
   pass

class Carro(Veiculo):
   pass

class Caminhao(Veiculo):
   def __init__(self, cor, placa, numero_rodas, carregado):
      super().__init__(cor, placa, numero_rodas) # para sobrescrever o que está na classe pai.
      self.carregado = carregado

   def esta_carregado(self):
      print(f"{'Sim' if self.carregado else 'Não'} estou carregado")


moto = Motocicleta("Branca", "ABC-1234", 2)
carro = Carro("Preto", "FPD-5987", 4)
caminhao = Caminhao("Azul", "FGV-4567", 6, True)

print(moto, carro, caminhao, sep="\n") #colocando dessa maneira ele exibi um embaixo do outro.