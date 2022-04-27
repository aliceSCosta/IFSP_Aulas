'''Crie um programa que dada uma sequência de N elementos fornecidos 
pelo usuário mostre a sequência original e a sequência elevada ao cubo.'''

lista = []

parada = 'c'
while parada != 's':
    num = input("Digite um número ou digite 's' para sair: " )
    
    if num == 's':
        parada = 's'
    else:
        lista.append(int(num))

cubo = []
for elemento in lista:
    cubo.append(elemento**3)

print(lista)
print(cubo)