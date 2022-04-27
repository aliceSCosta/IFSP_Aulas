# PECORRER UMA MATRIZ

# Com While
matriz = [[1, 2], [3, 4], [5, 6], [7, 8]]

row = 0
while row < len(matriz):
    print(f"Elementos da linha {row}")
    
    col = 0
    while col < len(matriz[row]):
        print(f"{matriz[row][col]}")

        col += 1
    
    row += 1


# Com for
for row in range(0, len(matriz)):
    print(f"Elementos da linha {row}")

    for col in range(0, len(matriz[row])):
        print(f"{matriz[row][col]}")