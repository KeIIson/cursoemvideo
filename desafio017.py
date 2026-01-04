from math import hypot
b = float(input('Cumprimento do Cateto Oposto:'))
h = float(input('Cumprimento do Cateto Adjacente:'))
hipotenusa = hypot (b,h)
print('A hipotenusa é {:.2f}'.format(hipotenusa))
