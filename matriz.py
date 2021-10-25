print("Preenchendo a matriz!\n")
linhas = int(input("Digite o numero de Linhas: "))
colunas = int(input("Digite o numero de Colunas: "))

matriz = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(int(input("Digite o valor da [" + str(i) + "][" + str(j) + "] - ")))
    matriz.append(linha)
for k in range(linhas):
    for l in range(colunas):
        print("%d" % matriz[k][l], end="")
    print("\n")
