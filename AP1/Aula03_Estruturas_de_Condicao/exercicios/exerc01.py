#Faça um programa que receba 5 números inteiros e informe o maior
#entre eles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))
num5 = int(input("Digite o quinto número: "))

if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
    print(num1, "é o maior")
elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
    print(num2, "é o maior")
elif num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5:
    print(num3, "é o maior")
elif num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:
    print(num4, "é o maior")
else:
    print(num5, "é o maior")