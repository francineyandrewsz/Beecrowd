#Importar sqrt (raiz quadrada) da biblioteca math
from math import sqrt
#Leia quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2)
x1, y1 = input().split(' ')
x1 = float(x1)
y1 = float(y1)
x2, y2 = input().split(' ')
x2 = float(x2)
y2 = float(y2)

#calcule a distância entre eles, segundo a fórmula
distância = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

#imprima o valor da distância com 4 casas após o ponto decimal
print(f'{distância:.4f}')

