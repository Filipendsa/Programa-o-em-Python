nota1 = float(input("Digite uma nota: "))
nota2 = float(input("Agora, digite a segunda nota: "))
media = (nota1 + nota2)/2
if media == 10:
    print("O aluno está APROVADO com Distinção e Honrarias!")
elif media >= 6:
    print("O aluno está APROVADO!")
elif media <6:
    print("O aluno está REPROVADO!")