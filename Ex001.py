nome = str(input('Qual seu nome?\n'))
altura = float(input('Qual a sua altura?\n'))
peso = float(input('QUal o seu peso?\n'))
imc = peso / altura**2

print(nome, ', calculei seu IMC e o resultado é:\n', imc)
