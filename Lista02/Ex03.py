num1 = int(input("Insira um número:  "))
num2 = int(input("Insira um número:  "))
max = 0
min = 0
if num1 > num2:
    max = num1
    min = num2
else:
    max = num2
    min = num1

for min in range(min,max):
    print("%d" %min)