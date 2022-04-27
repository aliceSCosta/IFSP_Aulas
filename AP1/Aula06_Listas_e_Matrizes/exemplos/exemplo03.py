matriz = []
numRow = int(input("Informe a quantidade de linhas da Matriz: "))
numCol = int(input("Informe a quantida de colunas da Matriz: "))

for i in range(numRow):
    listaRow = []
    print(f"Informe os elementos da linha {i}: ")
    
    for j in range(numCol):
        elem = int(input(f"Entre com o elemento da coluna {j}: "))
        listaRow.append(elem)
    
    matriz.append(listaRow)

for i in range(numRow):
    for j in range(numCol):
        print(matriz[i][j], end=" ")
    print("\n")