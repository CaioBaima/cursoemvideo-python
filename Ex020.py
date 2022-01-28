import random
aluno1 = str(input('Digite o nome de deus 4 alunos:\n'))
aluno2 = str(input())
aluno3 = str(input())
aluno4 = str(input())
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('A ordem sorteada para os alunos é:\n {}'.format(lista))
