class Bicicleta:

   def __init__(self, cor, modelo, ano, valor): #metódo constructor/inicializador
      self.cor = cor # self é atributo do objeto
      self.modelo = modelo #atributos da classe são as caracteristicas como cor, ano, modelo
      self.ano = ano
      self.valor = valor

   def buzinar(self):
      print("Plim plim...")     

   def parar(self):
      print("Parando a bicicleta...")
      print("Bicicleta parada!")

   def correr(self):
      print("Vrummmm...")

   # def __str__(self): # Método 1 para exibir a instância por completo com os valores 
   #    return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"
   
   def __str__(self): # Método 2 para exibir a instância por completo com os valores, diferente do método acima qualquer mudança na classe nao precisa mexer aqui.
      return f"{self.__class__.__name__}:{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


#Instância da Bicicleta
b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar() # seria o mesmo que chamar Bicicleta.buzinar(self) p
b1.correr()
b1.parar()
print(b1)