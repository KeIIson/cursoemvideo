nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome maiúsculas é: {}'.format(nome.upper()))
print('Seu nome minúsculas é: {}'.format(nome.lower()))
#print('Corta espaço:',nome.strip())
#print('Separado:',nome.split())
#dividido=''.join(nome.split())#retirando os espaços no nome
#nome.split() #separa o nome em partes
print('Seu nome ao todo tem {} letras:'.format(len(nome) - nome.count(' ')))
print('Quantidade de Caracteres:',len(nome))
#print('Seu primeiro nome tem:{} letras'.format(nome.find(' ')))
separa=nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0],len(separa[0])))
