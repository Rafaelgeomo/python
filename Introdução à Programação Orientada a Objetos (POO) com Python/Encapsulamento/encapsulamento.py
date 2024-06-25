class Conta:
   def __init__(self, nro_agencia, saldo=0):
      self._saldo=saldo #variavel publica
      self.nro_agencia = nro_agencia #variavel privada

   def depositar(self, valor): #método público
      self._saldo += valor

   def sacar(self, valor):
      self._saldo -= valor

   def mostrar_saldo(self):
      #mas nao seria tão simples assim aqui talvez teriamos que verificar n coisas para saber se esse pessoa poderia ter acesso ao saldo
      return self._saldo #acessar uma variavel privada criamos um método publico

conta = Conta("0001",100)
conta.depositar(100)
conta.sacar(150)
# conta._saldo += 100 # muito menos alterar o que ja estava declarado.
# print(conta._saldo) #ele irá acessar, mas nao é o correto pois pela convenção é um método privado.
print(conta.nro_agencia, conta.mostrar_saldo(), sep="\n")