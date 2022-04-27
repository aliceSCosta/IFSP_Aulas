# Fatias de lista

lista = ['a', 'b', 'c', 'd', 'e', 'f']

print(lista[1 : 3]) # [b, c]
print(lista[ : 4]) # [a, b, c, d]
print(lista[3 : ]) # [d, e, f]
print(lista[ : ]) # [a, b, c, d, e, f]

#-------------------------------------------------

#Inserindo elementos em uma lista com o operador SLICE

lista2 = ['a', 'd', 'f']
print(lista2)

lista[1 : 1] = ['b', 'c']
print(lista2)

lista[4 : 4] = ['e']
print(lista2)

#-------------------------------------------------

#Removendo elementos com o operador SLICE

del lista[1 : 5]
print(lista)

# OU

umaLista = ['a', 'b', 'c', 'd', 'e', 'f']

umaLista[1 : 3] = ['x', 'y']
print(umaLista)

umaLista[1 : 3] = []
print(umaLista)