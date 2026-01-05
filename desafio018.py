from math import radians,cos,tan,sin
angulo=float(input('Digite o ângulo que deseja:'))

angulo_radianos=radians(angulo)

seno_valor = sin(angulo_radianos)
cosseno_valor = cos(angulo_radianos)
tangente_valor = tan(angulo_radianos)

print('Ângulo: de {}° é {:.2f} radianos'.format(angulo,angulo_radianos))
print('Seno: {:.2f}'.format(seno_valor))
print('Cosseno: {:.2f}'.format(cosseno_valor))
print('Tangente: {:.2f}'.format(tangente_valor))