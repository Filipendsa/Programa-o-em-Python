numero = int(input("Digite um numero para ser fatorado: "))
resultado = 1
count = 1
while count <= numero:
    resultado *= count
    count += 1
print("Seu número Fatorado é: %"%resultado)