i = 0
num = []
soma = 0
while i < 5:
    numInsert = int(input("Insira o %dº número:  " % (i+1)))
    num.append(numInsert)
    soma = soma + numInsert
    i += 1
print("\nA soma dos números é: %d" %soma)
print("A média deles é: %d" %(soma/5))