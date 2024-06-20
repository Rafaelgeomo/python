class Animal:
   def __init__(self, nro_patas):
      self.nro_patas = nro_patas

   def __str__(self): # Método para exibir a instância por completo com os valores, diferente do método acima qualquer mudança na classe nao precisa mexer aqui.
      return f"{self.__class__.__name__}:{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
      def __init__(self, cor_pelo, **kw): #kwargs força vc a colocar chave e valor quando for chamar
         self.cor_pelo = cor_pelo         
         super().__init__(**kw)

class Ave(Animal):
      def __init__(self, cor_bico, **kw): 
         self.cor_bico = cor_bico
         super().__init__(**kw)

class Cachorro(Mamifero):
      pass   

class Ornitorrinco(Mamifero, Ave):
      pass

cachorro = Cachorro(nro_patas=4, cor_pelo="Branco e Marrom")
print(cachorro)

orni = Ornitorrinco(nro_patas=4, cor_bico="Cinza", cor_pelo="Preto")
print(orni)


class Foo:
   def hello(self):
      print(self.__class__.__name__.lower())


class Bar(Foo):
   def hello(self):
      return super().hello()


bar = Bar()
bar.hello()

