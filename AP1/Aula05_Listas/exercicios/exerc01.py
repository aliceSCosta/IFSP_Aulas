'''Faça um programa que crie uma lista com 10 números inteirosfornecidos pelo usuário. 
Após criar a lista, o programa deveráimprimir:
- O maior elemento da lista
- O menor elemento da lista
- A soma de todos os elementos da lista
- Os elementos ímpares
- Os elementos maiores do que 18
Obs: não use funções prontas.'''


lista = []

# Criando a lista a partir de valores dos usuários
while len(lista) != 10:
    lista.append(int(input("Digite um valor inteiro: ")))

print(lista)

maior = lista[0]
menor = lista[0]
soma = 0
impares = 0
maiorQue18 = 0

for elem in lista:
    
    #Procurar o maior valor da lista criada
    if elem > maior:
        maior = elem
    
    #Prucurar o menor elemento da lista
    if elem < menor:
        menor = elem

    #Soma de todos os elementods da lista
    soma += elem

    #Os elementos ímpares
    if elem % 2 != 0:
        impares += 1
    
    #Elementos maiores que 18
    if elem > 18:
        maiorQue18 += 1

   
print(f"O maior elemento da lista é {maior}")
print(f"O menor elemento da lista é {menor}")
print(f"A soma de todos os elementos da lista é {soma}")
print(f"A quantidade de números ímpares é {impares}")
print(f"A quantidade de elementos maiores que 18 é {maiorQue18}")