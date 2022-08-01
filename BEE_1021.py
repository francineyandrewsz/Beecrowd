'''Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.'''

valor = float(input())
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
cont = 0

print('NOTAS:')
for i in range(len(notas)):
    cont = valor // notas[i]
    valor %= notas[i]
    print(f'{cont:.0f} nota(s) de R$ {notas[i]:.2f}')

print('MOEDAS:')
for c in range(len(moedas)):
    cont = valor // moedas[c]
    valor %= moedas[c]
    print(f'{cont:.0f} moeda(s) de R$ {moedas[c]:.2f}')
    