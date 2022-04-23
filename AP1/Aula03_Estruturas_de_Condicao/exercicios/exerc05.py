#Crie um algoritmo para resolver equações do 2º grau.
#Considere:
#     ax2 + bx + c = 0 (a deve ser diferente de 0)
#     delta = b2 - 4 * a * c
#     Caso: delta < 0, não existe raiz real
#     delta = 0, existe uma raiz real: x = (-b) / (2 * a)
#     delta > 0, existem duas raízes reais:
#     x1 = (- b + raiz quadrada de delta) / (2 * a)
#     x2 = (- b - raiz quadrada de delta) / (2 * a)


import math #biblioteca matematica que fornece a funcao sqrt()  para calcular a raiz quadrada

a = int(input("Entre com o valor de a: "))

if a == 0:
    print("O valor de a não pode ser zero!")
else:
    b = int(input("Entre com o valor de b:"))
    c = int(input("Entre com o valor de c: "))
    delta = b**2 - 4*a*c

    if delta < 0:
        print("Não existe raiz real!")
    elif delta == 0:
        x = (-b) / (2*a)
        print(f"Há uma raiz real: {x}")
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print("Há uma raízes reais")
        print(f"Raíz 1: {x1}")
        print(f"Raíz 2: {x2}")