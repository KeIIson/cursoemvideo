reais=float(input('Quantos reais você tem?\n'))
cambio= reais / 5.52
print('O dolar está $5,52\n')
print('Você tem R${:.2f} reais, logo você pode comprar US${:.2f}.'.format(reais,cambio))