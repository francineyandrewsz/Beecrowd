#Ler 2 valores de ponto flutuante de dupla precisão A e B
a = float(input())
b = float(input())

#cálculo da média dos valores de A e B, sabendo que A tem peso 3.5 e B tem peso 7.5
media = ((a*3.5)+(b*7.5))/(3.5+7.5)

#imprimir o resultado com a mensagem "MEDIA" e média do aluno com 5 dígitos após o ponto decimal
print(f'MEDIA = {media:.5f}')
