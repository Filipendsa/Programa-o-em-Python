decisao = 1
while (decisao != 0):
      nota = int(input("Selecione um númeo de 0 a 10: "))
      if nota > 10 or nota < 0:
            print("Número inválido. Por favor, insira um número de 0 a 10!")
      else:
            print("Seu número é Valido. %d" % nota)
            decisao = 0
else:
      print("Loop foi encerrado com sucesso!")