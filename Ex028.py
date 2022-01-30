print('Pensei em um número aleatório entre 0 e 5')
import random
num = random.randint(0, 5)
adivinha = int(input('Digite um número entre 0 e 5 e veja se acertou.\n'))
if num == adivinha:
    print('Você acertou')
else:
    print('Você errou, pensei no número {}'.format(num))
