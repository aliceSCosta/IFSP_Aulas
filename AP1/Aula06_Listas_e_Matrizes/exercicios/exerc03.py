'''Faça um programa que solicite do usuário um valor N, representando
a dimensão de uma matriz quadrada (matriz A). Em seguida, o
programa deverá solicitar do usuário os elementos da matriz A e,
posteriormente, deverá verificar se A é simétrica. Obs: Matriz
simétrica: matriz quadrada de ordem n tal que A = At'''


matriz = []
numRow = int(input("Informe a quantidade de linhas que a matriz terá: "))
numCol = int(input("Informe a quantidade de colunas que a matriz terá: "))

for i in range(0, numRow):
    linha = []
    for j in range(0, numCol):
        elem = int(input(f"Informe o número da linha {i} coluna {j}: "))
        linha.append(elem)
    matriz.append(linha)

print(matriz)

