salario = float(input("Digite O salario: "))
if salario <= 280:
    reajuste = 0.2
elif salario > 280 and salario <= 700:
    reajuste = 0.15
elif salario > 700 and salario <= 1500:
    reajuste = 0.1
elif salario > 1500:
    reajuste = 0.05
print("\nReajustando o seu salário de Seu Salário...\n")
print("Seu Antigo salario era de: %d" % salario)
print("Seu Percentua de aumento foi de: %.2f" % reajuste)
print("Seu Valor de aumento foi de: %.2f" % (salario * reajuste))
print("Seu Novo salario é de: %d" % (salario + (salario * reajuste)))