'''Crie um programa que leia inicialmente uma sequência de N números
inteiros e ao seu final mostre a sequência original, a soma de seus
elementos que forem pares e a multiplicação dos elementos que forem ímpares.'''

listaInteiros = []

parada = 'c'
while parada != 's':
    numero = input('Informe um número inteiro ou digite "s" para sair: ')

    if numero == 's':
        parada = 's'
    else:
        listaInteiros.append(int(numero))


if len(listaInteiros) > 0:
    soma = 0
    multiplicacao = 1

    for i in listaInteiros:
        if i % 2 == 0:
            soma += i
        else:
            multiplicacao *= i

    print(listaInteiros)
    print(f"A soma dos números pares da lista é {soma}")
    print(f"A multiplicação dos números ímpares da lista é {multiplicacao}")
