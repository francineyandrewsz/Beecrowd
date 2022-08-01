'''Leia um valor inteiro correspondente à idade de uma pessoa e
informe-a em anos, meses e dias'''
 
valor = int(input())

ano = valor // 365
valor = valor - ano * 365

mes = valor // 30
valor = valor - mes * 30

dias = valor 

print(f'{ano:.0f} ano (s)\n{mes:.0f} mes (es)\n{dias:.0f} dia (s)')
