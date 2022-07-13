#Leia 3 valores, no caso, variáveis A, B e C
a = float(input())
b = float(input())
c = float(input())

#Calcule a média sabendo que A tem peso 2, B tem peso 3 e C tem peso 5
média = ((a*2)+(b*3)+(c*5))/(2+3+5)

#Imprima a mensagem "MEDIA" e a média com 1 dígito após o ponto decimal
print(f'MEDIA = {média:.1f}')
