i = 0
num = []
soma = 0
numPar = 0
numImpar = 0
for i in range(20):
    numInsert = int(input("Insira o %dº número:  " % (i+1)))
    if ((numInsert%2) == 0):
        numPar +=1
    else:
        numImpar +=1

print("Quantidade de números pares: %d" %numPar)
print("Quantidade de números ímpares: %d" %numImpar)