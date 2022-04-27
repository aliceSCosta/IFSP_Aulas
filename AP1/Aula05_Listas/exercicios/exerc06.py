'''Crie um programa que leia inicialmente duas sequências de N elementos cada 
uma e ao final mostre as duas sequências originais e a sequência resultante 
da soma de seus elementos. Exemplo:
a=[5, 9, 0] b=[12, 34, 101] soma=[17, 43, 101]'''

parcela1 = []
parcela2 = []

parada1 = 'c'
while parada1 != 's':
    num = input('Digite o valor da parcela 1 ou digite "s" para sair: ')

    if num == 's':
        parada1 = 's'
    else:
        parcela1.append(int(num))


while len(parcela2) != len(parcela1):
    num = int(input('Digite o valor da parcela 2 (ATENÇÃO! O programa ' +
    'só encerrará quando a quantidade de elementos da parcela 2 for a mesma da parcela 1): '))

    parcela2.append(num)

soma = []
totalElementos = len(parcela1)
for i in range(0, totalElementos):
    soma.append(parcela1[i] + parcela2[i])

print(parcela1)
print(parcela2)
print(soma)