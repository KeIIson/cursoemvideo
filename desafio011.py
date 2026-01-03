pv=float(input('Quantos metros tem a vertical da parede?'))
ph=float(input('Quantos metros tem a horizontal da parede?'))
area=pv*ph
tinta=area/2
print('Para pintar a parede de {:.3f}m².\nPrecisamos de {:.3f}L de tinta.'.format(area,tinta))