nota = []
nome = []
cont = 0
opcao = " "
soma = 0
while opcao.upper() != 'N':
    nome.append(input("Digite o nome do %d aluno: " % (cont + 1)))
    nota.append(float(input("Digite a nota do %d Aluno: " % (cont + 1))))
    soma += nota[cont]
    opcao = input("Gostaria de adicionar mais registros no nosso banco? (S -> Sim; N -> Não)")
    cont +=1