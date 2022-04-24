import math #biblioteca matematica que fornece a funcao sqrt()  para calcular a raiz quadrada

a = 0

while a == 0:   
    a = int(input("Entre com o valor de a: "))


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
