#Leia três valores com ponto flutuante de dupla precisão A, B e C
a, b, c = input().split(' ')
a = float(a)
b = float(b)
c = float(c)

#O valor de pi
pi = 3.14159

#A área do triângulo retângulo que tem A por base e C por altura
tri = a*c/2
#A área do círculo de raio C (pi=3.14159)
cir = pi*c*c
#A área do trapézio que tem A e B por bases e C por altura
trap = (a*b)/2.0*c
#A área do quadrado que tem lado B
qua = b*b
#A área do retângulo que tem lados A e B
ret = a*b

#Imprima o arquivo com 5 linhas e o valor calculado deve ser apresentado com 3 dígitos após o ponto decimal
print(f'TRIANGULO: {tri:.3f}\nCIRCULO: {cir:.3f}\nTRAPEZIO: {trap:.3f}\nQUADRADO: {qua:.3f}\nRETANGULO: {ret:.3f}')
