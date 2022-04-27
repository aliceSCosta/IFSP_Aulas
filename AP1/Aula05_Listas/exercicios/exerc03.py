'''Crie um programa que leia inicialmente uma sequência de N notas dealunos fornecidas 
pelo usuário e ao final mostre a sequência e suamédia aritmética. 
Defina um critério de parada para a entrada denotas pelo usuário.'''

listaNotas = []

parada = 0
while parada != -1:
    nota = float(input("Informe a nota do aluno ou digite -1 para sair: "))

    if nota == -1:
        parada = -1
    else: 
        listaNotas.append(nota)

if len(listaNotas) > 0:
    print(listaNotas)

    soma = 0
    for i in listaNotas:
        soma += i

    media = soma / len(listaNotas)
    print(f"A média do aluno é {media}")
