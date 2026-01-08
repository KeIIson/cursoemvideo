nome = str(input('Digite seu nome completo:'))
print('Maiusculo:',nome.upper())
print('Minusculo',nome.lower())
print('Corta espaço:',nome.strip())
print('Separado:',nome.split())
dividido=''.join(nome.split())#retirando os espaços no nome
result=nome.split() #separa o nome em partes
print('Quantidade de letras:',len(dividido))
print('Quantidade de Caracteres:',len(nome))
print('Quantidade de letras primeiro nome:', len(result[0]))
