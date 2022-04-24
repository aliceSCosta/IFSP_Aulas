#Faça um programa que leia um número inteiro > 0 e calcule o seu fatorial.

num = int(input("Informe um número inteiro: "))

fatorial = 1

#Com while
contador = 1
while contador <= num:
    fatorial *= contador
    contador += 1


#Com for
for i in range(1, num+1):
    fatorial *= i



print(f"O fatorial de {num} é {fatorial}")