salario=int(input('Qual valor do seu salário? R$\n'))
aumento=salario+(15*salario/100)
print('Você receberá um aumento de 15%!\n\nSeu salário agora será R${:.2f}'.format(aumento))