#Desempacotamento de listas em variáveis

# Números inteiros
x, y, z = [1, 2, 3]

print(x)
print(y)
print(z)

# Cadeia de caracteres
n1, n2 = ["marcos", "joão"]
print(n1)
print(n2)

# Descartar valores
x, y, _ = [1, 2, 3]
print(x)
print(y)

#--------------------------------------------------------------------

#Desempacotamento em sequencias

notas = [9, 7, 8, 5, 10, 20, 30]

n1, *n2 = notas

print(n1)
print(n2)

first, *_, last = notas

print(first)
print(last)