'''Crie um programa que leia inicialmente uma sequência de N números inteiros 
fornecidos pelo usuário e mostre ao final da leitura a sequência original e a sequência invertida.'''

lista = []

parada = 'c'
while parada != 's':
    num = input("Informe um número ou digite 's' para sair: ")

    if num == 's':
        parada = 's'
    else:
        lista.append(int(num))


print(lista)


for i in range(0, len(lista)):
    lista = lista[::-1]

print(lista)