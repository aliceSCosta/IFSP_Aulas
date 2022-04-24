#Faça um programa para mostrar a tabuada de um número qualquer
#fornecido pelo usuário.

num = int(input("Entre com o número para a tabuada: "))

#Com while
x = 1

while x <= 10:
    print(num, " x ", x, " = ", num*x)
    x += 1



#Com for
for x in range(1, 11):
    print(num, "x", x, "=", num*x)