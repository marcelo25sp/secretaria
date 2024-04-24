print('Secretaria Escola Futuro')
print('*'*100)
aluno = input('Digite o nome do aluno: ')
print('Bem vindo', aluno)
n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
media = (n1 + n2)/2
print('A média do aluno {} é {}'.format(aluno,media))

if media >= 7:
    print('Aluno aprovado!')
else:
    print('Aluno reprovado')





