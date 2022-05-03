'''Crie um programa que solicita do usuário um valor N representando a
quantidade linhas e um valor M representando a quantidade de colunas
de uma matriz. Depois, o programa deverá solicitar do usuário N x M
elementos para serem incluídos na matriz. Por fim, o programa deverá
percorrer a matriz para encontrar e imprimir o seu maior elemento e o
seu menor elemento.'''

matriz = []
numRow = int(input("Informe a quantidade de linhas da matriz: "))
numCol = int(input("Informe a quantidade de colunas da matriz: "))

i = 0
while i < numRow:
    linha = []

    j = 0
    while j < numCol:
        elem = int(input("Informe um número: "))
        linha.append(elem)

        j += 1

    matriz.append(linha)
    i += 1

maior = matriz[0][0]
menor = matriz[0][0]

for i in range(numRow):
    for j in range (numCol):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
        elif matriz[i][j] < menor:
            menor = matriz[i][j]
        print(matriz[i][j], end=" ")
    print("\n")
#usar elif para juntar os dois for


print(f"O maior elemento da matriz é {maior}")
print(f"O menor elemento da matriz é {menor}")



#============= CORREÇÃO ===============#

matriz = []
numRow = int(input("Informe a quantidade de linhas da matriz: "))
numCol = int(input("Informe a quantidade de colunas da matriz: "))

i = 0
while i < numRow:
    linha = []

    j = 0
    while j < numCol:
        elem = int(input("Informe um número: "))
        linha.append(elem)

        j += 1

    matriz.append(linha)
    i += 1

maior = matriz[0][0]

i = 0
while i < numRow:
    j = 0
    while j < numCol:
        if matriz[i][j] > maior:
            maior = matriz[i][j]
        j += 1
    
    i += 1

print(f"Maior valor da matriz {maior}")

menor = matriz[0][0]

#***** continua