v=float(input('Digite o valor do produto: R$'))
desc= 0.05*v
total=v-desc

print('Seu produto recebeu 5% de desconto!\n')
print('Valor com desconto:{:.2f} reais'.format(total))