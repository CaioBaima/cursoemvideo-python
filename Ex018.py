import math
ang = int(input('Digite um ângulo:\n'))
print('O valor de seu seno é {:.2f}, de seu cosseno é {:.2f} '
      'e de sua tangente é {:.2f}'.format(math.sin(math.radians(ang)), math.cos(math.radians(ang)),
                                      math.tan(math.radians(ang))))
