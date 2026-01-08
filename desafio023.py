"""num=str(input('Digite um valor entre 0 e 9999:'))
#usar []  permite fatiar os números em uma string
print('Milhar:',num[0])
print('Centena:',num[1])
print('Dezena:',num[2])
print('Unidade:',num[3])"""

#Convertendo INT para STRING antes do resultado
num=int(input('Digite um número entre 0 e 9999:'))
digitado=[int(n)for n in str(num)]
print('Milhar:',digitado[0])
print('Centena:',digitado[1])
print('Dezena:',digitado[2])
print('Unidade:',digitado[3])