'''Faça um programa em Python que receba dois valores inteiros,representando a base e o expoente. 
O programa deverá calcular e apresentar o resultado da base elevada ao expoente. Por exemplo, para
base = 5 e expoente = 3, ou seja, 53, o programa deverá imprimir 125.
Obs: não utilize o operador de exponenciação (**). Utilize somente estrutura de
repetição.'''


base = int(input("Informe a base: "))
expoente = int(input("Informe o expoente: "))
resultado = base

#Com while
count = 1
while count < expoente:
    resultado = base * resultado
    count += 1
print("O resultado da potência é: ", resultado)


#Com  for
for i in range(1, expoente):
    resultado = base * resultado
print("O resultado da potência é: ", resultado)