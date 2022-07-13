#Ler o nome de um vendedor
nome = str(input())
#Ler o seu salário fixo
salário = float(input())
#O total de vendas efetuadas por ele no mês
vendas = float(input())

#Calcular o total a receber no final do mês 
total = salário + (vendas * 15 / 100)

#Imprima o total que o funcionário deverá receber
print(f'TOTAL = R$ {total:.2f}')
