def calculadora(operacao):
   def soma(a,b):
      return a+b
   
   def sub(a,b):
      return a-b
   
   def mult(a,b):
      return a*b
   
   def div(a,b):
      return a/b
   
   match operacao:
      case "+":
         return soma
      case "-":
         return sub
      case "*":
         return mult
      case "/":
         return div
      
#pode ser dessa maneira ou da maneira a seguir
# print(calculadora("+")(2,3))
# print(calculadora("-")(2,3))
# print(calculadora("*")(2,3))
# print(calculadora("/")(2,3))

#pode ser assim guardando a calculadora em uma variavel e imprimindo a variavel e passando os argumentos
op = calculadora("+")
print(op(2,3))
op = calculadora("-")
print(op(2,3))
op = calculadora("*")
print(op(2,3))
op = calculadora("/")
print(op(2,3))
