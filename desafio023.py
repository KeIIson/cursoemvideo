"""num=str(input('Digite um valor entre 0 e 9999:'))
#usar []  permite fatiar os números em uma string
print('Milhar:',num[0])
print('Centena:',num[1])
print('Dezena:',num[2])
print('Unidade:',num[3])"""

#Convertendo INT para STRING antes do resultado
"""num=int(input('Digite um número entre 0 e 9999:'))
digitado=[int(n)for n in str(num)]
print('Milhar:',digitado[0])
print('Centena:',digitado[1])
print('Dezena:',digitado[2])
print('Unidade:',digitado[3])"""

num  = int(input('Digite um número: '))
u = num  // 1 % 10 # dessa forma os divisores apresentarão o valor por casa
d = num // 10 % 10 #dezena
c = num // 100 % 10 #centena
m = num // 1000 % 10 #milhar
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))