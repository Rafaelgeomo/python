class Bicicleta:

   def __init__(self, cor, modelo, ano, valor): #metódo constructor
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

   # def __str__(self):
   #    return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"


#Instância da Bicicleta
b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar() # seria o mesmo que chamar Bicicleta.buzinar(self) p
b1.correr()
b1.parar()
print(b1)