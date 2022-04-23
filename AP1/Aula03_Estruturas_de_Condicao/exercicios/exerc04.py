#Faça um algoritmo que receba três valores A, B e C e verifica se
#eles podem ser os comprimentos dos lados de um triângulo. Se
#forem, mostrar se é um triângulo equilátero, isósceles ou escaleno.
#Considere que:
# - Para ser triângulo: cada lado é menor que a soma dos outros dois
#lados.
# - Triângulo equilátero: tem três lados iguais
# - Triângulo isósceles: tem dois lados iguais e um diferente
# - Triângulo escaleno: tem três lados diferentes

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

if a < (b+c) and b < (a+c) and c < (a+b):

    if a == b and a == c:
        print("É um triângulo equilátero.")
    elif a == b or a == c or b == c:
        print("É um triângulo isósceles")
    else:
        print("É um triângulo escaleno")
else:
    print("Não é um triângulo")