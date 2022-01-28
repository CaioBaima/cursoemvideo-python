import math
cat1 = float(input('Digite o valor do cateto adjacente:\n'))
cat2 = float(input('Digite o valor da hipotenusa:\n'))
hip = math.hypot(cat1, cat2)
print('O valor referente a hipotenusa é {}'.format(hip))
