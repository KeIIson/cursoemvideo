print('Vou verificar se sua cidade começa com SANTO')
santo=str(input('Digite o nome da sua cidade:')).strip()
positivo = 'SANTO' in santo.upper()
print('{}!'.format(positivo))