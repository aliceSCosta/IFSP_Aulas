#Faça um programa que mostre os 8 primeiros termos da sequência de
#Fibonacci. Ex: 0, 1, 1, 2, 3, 5, 8,13, 21,34, 55...

termo1 = 0
termo2 = 1
sequencia = 0

#Com while
contador = 1
while contador <= 8:
    print(sequencia)
    termo1 = termo2
    termo2 = sequencia
    sequencia = termo1 + termo2

    contador += 1

#Com for
for i in range(1, 9):
    print(sequencia)
    termo1 = termo2
    termo2 = sequencia
    sequencia = termo1 + termo2