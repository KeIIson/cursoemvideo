print('Verificando quantidade de letras A:')
a=str(input('Digite uma informação:'))


print('A letra "A" aparece {} vezes'.format(a.count('A')))
print('A posição do primeiro "A":', a.find('A'))

ultimo = a.rfind ('A')
print('A posição do último "A":', ultimo)