#O tempo gasto em horas
tempo = int(input())
#A velocidade média durante a mesma em (Km/h) 
velocidade = int(input())

#calcular e mostrar a quantidade de litros de combustível gastos em uma viagem, ao utilizar um automóvel que faz 12 KM/L
automóvel = (tempo * velocidade) / 12

#Imprima a quantidade de litros necessária para realizar a viagem, com três dígitos após o ponto decimal
print(f'{automóvel:.3f}')
