'''Faça um programa que solicite do usuário um valor N, representando a
dimensão de uma matriz quadrada (matriz A). Em seguida, o programa
deverá solicitar do usuário os elementos da matriz A e, posteriormente,
deverá criar a matriz transposta de A (At). Ao final, deve ser mostrada a
matriz original e sua respectiva transposta. Lembre-se que a matriz
transposta At será obtida a partir da matriz A trocando-se
ordenadamente as linhas por colunas (ou as colunas por linhas).'''

matriz = []
numRow = int(input("Informe a quantidade de linhas que a matriz terá: "))
numCol = int(input("Informe a quantidade de colunas que a matriz terá: "))

for i in range(0, numRow):
    linha = []
    for j in range(0, numCol):
        elem = int(input(f"Informe o elemento da linha {i} coluna {j}: "))
        linha.append(elem)
    matriz.append(linha)

print(matriz)


matrizTransposta = []
i = 0
while i < numRow:
    linha = []
    j = 0
    while j < numCol:
        linha.append(matriz[j][i])
        j += 1

    matrizTransposta.append(linha)
    i += 1

print(matrizTransposta)