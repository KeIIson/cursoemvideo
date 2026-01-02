medida=float(input('Digite uma distância em metros: '))
km=medida/1000 #quilometros
hm=medida/100 #hectometros
dam=medida/10 #decametros
dm=medida/1 #decimetros
cm= medida*100 #centimetros
mm=medida*1000 #milimetros
print('O valor de {} em cm é {:.0f} cm'.format(medida,cm))
print('{:.0f} km'.format(km))
print('{:.0f} hm'.format(hm))
print('{:.0f} dam'.format(dam))
print('{:.0f} dm'.format(dm))
print('{:.0f} cm'.format(cm))
print('{:.0f} mm'.format(mm))