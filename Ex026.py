frase = str(input('Digite uma frase:\n')).upper().strip()
print('Sua frase possui {} letras (a)'.format(frase.count('A')))
print('O primeiro aparece na posição {}'.format(frase.find('A') + 1))
print('O último aparece na posição {}'.format(frase.find('A', -1) + 1))
