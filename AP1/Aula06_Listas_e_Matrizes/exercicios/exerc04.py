'''Faça um programa que solicite do usuário um valor N, representando
a dimensão de uma matriz quadrada (matriz A). Em seguida, o
programa deverá solicitar do usuário os elementos da matriz A e,
posteriormente, deverá verificar se A é simétrica. Obs: Matriz
simétrica: matriz quadrada de ordem n tal que A = At''''''Faça um programa que solicite do usuário um valor N, representando
a dimensão de uma matriz quadrada (matriz A). Em seguida, o
programa deverá solicitar do usuário os elementos da matriz A e,
posteriormente, deverá verificar se A é simétrica. Obs: Matriz
simétrica: matriz quadrada de ordem n tal que A = At'''

dimensao = int(input('Qual será a dimensão da matriz? '))

matriz = []
for i in range(dimensao):
    linha = []
    for j in range(dimensao):
        elem = int(input(f"Informe o número da linha {i} coluna {j}: "))
        linha.append(elem)
    matriz.append(linha)

print(matriz)


matrizTransposta = []
i = 0
while i < dimensao:
    linha = []
    j = 0
    while j < dimensao:
        linha.append(matriz[j][i])
        j += 1

    matrizTransposta.append(linha)
    i += 1

print(matrizTransposta)

if matriz == matrizTransposta:
    print("A matriz é simétrica")
else:
    print("A matriz não é simétrica")