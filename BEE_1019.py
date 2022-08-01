'''Leia um valor inteiro, que é o tempo de duração em segundos
de um determinado evento em uma fábrica, e informe-o expresso no
formato horas:minutos:segundos.'''

#Entrada com valor inteiro
n = int(input())

h = n // 3600
m = (n - (h * 3600)) // 60
s = n % (24 * 3600)
s %= 3600
s %= 60

#Imprima com a entrada (segundos), convertido para h:m:s
print(f'{h:.0f}:{m:.0f}:{s:.0f}')


