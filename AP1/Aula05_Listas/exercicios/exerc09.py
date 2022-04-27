'''Crie um programa que leia inicialmente uma sequência de N elementos inteiros 
positivos fornecidos pelo usuário e substitua seus elementos de valor ímpar por -1 e os pares por +1. 
Ao final imprima a sequênciaoriginal e a sequência alterada.'''

lista = []

parada = 'c'
while parada != 's':
    num = input("Informe um número ou digite 's' para sair: ")

    if num == 's':
        parada = 's'
    elif int(num) >= 0:
        lista.append(int(num))
    else:
        print("Digite um valor positivo")

print(lista)

lista2 = []
for elemento in lista:
    if elemento % 2 == 0:
        lista2.append(+1)
    else:
        lista2.append(-1)

print(lista2)