i = 0
num = []
decisao = 1
while decisao != 0:
    numInsert = int(input("Insira o %dº número:  " % (i + 1)))
    num.append(numInsert)
    if ((numInsert % 2) != 0):
        print("Esse número - %d - é impar" % numInsert)
    decisao = int(input("Quer continuar a adicionar valores? (1 - Sim; 0 - Não)"))
    i += 1

print(num)