#Gere uma lista de contendo os múltiplos de 3 entre 1 e 150.

lista = []

for i in range(1, 151):
    if i % 3 == 0:
        lista.append(i)
    
print(lista)