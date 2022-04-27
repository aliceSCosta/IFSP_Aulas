print("Pertinencia em uma lista")

frutas = ['maçã', 'laranja', 'banana', 'cereja']

print('maçã' in frutas) #imprime TRUE
print('pera' in frutas) #imprime FALSE
print('morango' not in frutas) #imprime TRUE

print("-----------------------------------------------------------------------")

print("Comprimento de listas") 

lista = [3, 67, "gato", 56, 808, 3.14, False]
print(len(lista)) # imprime o valor 7

print("-----------------------------------------------------------------------")

print("Concatenação")

print([1 , 2] + [3, 4])
print(frutas + [6, 7, 8, 9])

lista_orig = [45, 32, 88]
lista_orig = lista_orig + ["cachorro"]
print(lista_orig)

print("-----------------------------------------------------------------------")

print("Inserir um elemento no final de uma lista")

frutas.append('acerola')
print(frutas)

print("Inserindo uma sublista") 

lista_orig.append("gato")
lista_orig.append(["cachorro"]) # outra lista
print(lista_orig)

print("-----------------------------------------------------------------------")

print("Função id()")

lista2 = [4, 5, 6]
print(id(lista2))

print("------------------------------------------------------------------------")

print("Inserir um elemento em determinada posição")

cavaleiros = ['guerra', 'fome', 'peste']

cavaleiros.insert(1, 'morte')
print(cavaleiros)

print("------------------------------------------------------------------------")

print("Remover um elemento de uma lista")

del cavaleiros[2]
print(cavaleiros)

print("------------------------------------------------------------------------")

print("Replicando elementos de uma lista")

print([0] * 4)
print([1, 2, "Olá, tudo bem?" * 2])