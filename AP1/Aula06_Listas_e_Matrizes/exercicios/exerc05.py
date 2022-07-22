'''Escreva um programa que leia inteiros positivos m e n e os elementos
de uma matriz A de números inteiros de dimensão m x n e ao final
mostra a quantidade de linhas e colunas que tem apenas zeros (linhas
nulas e colunas nulas).'''

dimensao = int(input('Informe a dimensão da matriz: '))
 
matriz = []

for i in range(dimensao):
    linha = []
    
    for j in range(dimensao):
        numCol = int(input(f'Informe um inteiro para a linha {i} coluna {j}'))
        if numCol >= 0:
            linha.append(numCol)
        else:
            print('Informe um número inteiro maior ou igual a 0')
    
    matriz.append(linha)


colunasZero = 0
linhasZero = 0

for linha in matriz:
    for coluna in linha:
        if coluna == 0:
            colunasZero += 1
if colunasZero == dimensao:
    linhasZero += 1
    
print('Números de linhas nulas: ', linhasZero)