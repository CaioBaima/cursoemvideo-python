largura = float(input('Digite a largura da parede:\n'))
altura = float(input('Digite a altura da parade:\n'))
área = largura * altura
print('A área da sua parede é {}m²'.format(área))
print('Serão necessários {}L de tinta'.format(área/2))
print('Serão necessários {} baldes de tinta'.format(área//2))
print('Sobram {}m² de parede para pintar'.format(área % 2))
