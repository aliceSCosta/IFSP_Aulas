#Faça um programa que exiba todos os números de 1 a 100 que são
#divisíveis por 7.


#Com while
x = 1

while x <= 100:
    if x % 7 == 0:
        print(x)
    x += 1


#Com for
for x in range (1, 101):
    if x % 7 == 0:
        print(x)
    