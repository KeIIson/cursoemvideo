km=float(input('Quantos Km rodados?'))
dias=int(input('Quantos dias foram alugados?'))
pago = (dias * 60) + (km *0.15)
print('O total a pagar é de {:.2f}'.format(pago))