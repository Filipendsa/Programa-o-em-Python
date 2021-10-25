base = int(input("Insira um número para base:  "))
expoente = int(input("Insira um número para ser o expoente:  "))
resultado = 1
for i in range(expoente):
    resultado *= base

print("O resultado é: %d" % resultado)