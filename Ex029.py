vel = int(input('Você estava dirigindo a quantos Km/h?\n'))
multa = (vel - 80) * 7
if vel <= 80:
    print('Parabéns, não ultrapassou o limite de velocidade.')
else:
    print('Você deverá pagar uma multa no valor de:\n R${:.2f}'.format(multa))
