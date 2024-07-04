def principal():
   print("Executando a funcao principal")

   def funcao_interna():
      print("Executando a funcao interna")

   def funcao_interna2():
      print("Executando a funcao interna 2")

   funcao_interna()
   funcao_interna2()

principal()