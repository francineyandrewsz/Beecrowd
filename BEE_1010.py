#Ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1
a, b, c = input().split(' ')
a = int(a)
b = int(b)
c = float(c)

#Ler o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2
d, e, f = input().split(' ')
d = int(d)
e = int(e)
f = float(f)

#Calcule o valor a ser pago
p1 = b*c
p2 = e*f

#Imprimir uma mensagem com o valor ser apresentado
print(f'VALOR A PAGAR: R$ {p1+p2:.2f}')
