cavaleiros = ['guerra', 'fome', 'peste', 'morte']

# Percorrendo uma lista por ELEMENTO (usado quando o indice não importa e vc só quer pegar o valor)
for elem in cavaleiros:
    if elem == 'fome':
        print (elem)

#-----------------------------------------------------------------------------------------------------------

# Percorrendo uma lista por ÍNDICE (usado quando o indice importa e vc precisa dele ex: uma lista ordenada)

#Com for

for i in range(len(cavaleiros)):
    print(cavaleiros[i])

#Com while
i = 0
while i < len(cavaleiros):
    print(cavaleiros[i])
    i+= 1

print ('Tamanho da lista: ', len(cavaleiros))


L = list(range(1, 20, 2))#valor inicial - valor limite exclusivo - intervalo
print(L)


for i in range(len(L)):
    print(L[i])

