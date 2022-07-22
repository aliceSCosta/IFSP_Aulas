'''# CÓPIA x REFERENCIA

# Neste exemplo, o valor do indice irá ser substituido nas duas listas
a = [0, 1, 2, 3, 4]
b = a
b[1] = 7
print("a = ", a)
print("b = ", b)


# Para fazer um clone independete siga o exemplo:
c = [0,1,2,3,4]
d = c[:]
d[1] = 7
print("c = ", c)
print("d = ", d)'''