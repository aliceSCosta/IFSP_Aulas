#Faça um programa que receba dois inteiros x e y e calcule o valor de z, dado pela expressão a seguir:
#z = (x**2+y**2) / (x-y)**2

x = int(input("Informe o valor de x: "))
y = int(input("Informe o valor de y: "))

z = (x**2 + y**2) / (x - y)**2

print("O resultado de z é: ", z)