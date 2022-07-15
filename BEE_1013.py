#Leia três valores
a, b, c = input().split(' ')
a = int(a)
b = int(b)
c = int(c)

#Cálculo através da fórmula pra saber qual é o maior
maior_AB = (a+b+abs(a-b))/2
maior_ABC = (maior_AB+c+abs(maior_AB-c))/2

#Imprima o maior número
print(f'{maior_ABC:.0f} eh o maior')
