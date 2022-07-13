#Leia o número de um funcionário
n = int(input())
#Seu número de horas trabalhadas
hrs = int(input())
#O valor que recebe por hora
valor = float(input())

#Calcula o salário desse funcionário
salário = hrs * valor

#Impima o número e o salário do funcionário
print(f'NUMBER = {n}\nSALARY = U$ {salário:.2f}')
