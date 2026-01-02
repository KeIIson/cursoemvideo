pv=int(input('Quantos metros tem a vertical da parede?'))
ph=int(input('Quantos metros tem a horizontal da parede?'))
area=pv*ph
tinta=area/2
print('Para pintar a parede de {} metros precisamos de {} litros de tinta.'.format(area,tinta))