'''Crie um programa que leia inicialmente uma sequencia de N númerosinteiros. 
Depois, o programa deve gerar e mostrar 2 novas listas apartir da primeira: 
uma sem repetição de elementos e outra com os elementos que se repetem na lista original.'''

listaInteiros = []

parada = 'c'
while parada != 's':
    inteiro = input("Digite um número inteiro ou 's' para sair")

    if inteiro == 's':
        parada = 's'
    else:
        listaInteiros.append(int(inteiro))

print(listaInteiros)

 
semRepeticao = []
comRepeticao = []
for elemento in listaInteiros:
    if elemento not in semRepeticao:
        semRepeticao.append(elemento)
    elif elemento not in comRepeticao:
        comRepeticao.append(elemento)

print(semRepeticao)
print(comRepeticao)