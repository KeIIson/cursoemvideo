import math
angulo=float(input('Digite o angulo para converter ao radiano:'))

angulo_radianos=math.radians(angulo)

seno_valor = math.sin(angulo_radianos)
cosseno_valor = math.cos(angulo_radianos)
tangente_valor = math.tan(angulo_radianos)

result_angulo = math.degrees(angulo_radianos)
print('Ângulo: de {}° é {:.4f} radianos'.format(angulo,angulo_radianos))
print('Seno: {:.4f}'.format(seno_valor))
print('Cosseno: {:.4f}'.format(cosseno_valor))
print('Tangente: {:.4f}'.format(tangente_valor))