'''Faça um programa em Python que leia um conjunto de valores
correspondentes às notas que os alunos obtiveram em uma prova de
Algoritmos. Quando o valor fornecido for um número negativo, significa
que não existem mais notas para serem lidas. Após isso seu programa
deverá:
- Escrever quantas notas são maiores ou iguais a 6.0
- Escrever quantas notas são maiores ou iguais a 4.0 e menores que 6.0
- Escrever quantos notas são menores que 4.0
- Escrever a média das notas fornecidas pelo usuário.'''


nota = 0
maiorSeis = 0
entreQuatroSeis = 0
abaixoQuatro = 0
somaNota = 0
count = 0

while nota >= 0:
    nota = int(input("Informe uma nota do aluno: "))
    if nota >= 6:
        maiorSeis += 1 
    elif nota >= 4 and nota < 6:
        entreQuatroSeis += 1
    else:
        abaixoQuatro += 1

    somaNota += nota
    count += 1 
    

media = somaNota / count

print("Total de notas maiores que 6.0: ", maiorSeis)
print("Total de notas entre 4.0 e 6.0: ", entreQuatroSeis)
print("Total de notas menores que 4.0: ", abaixoQuatro)
print("A média do aluno é: ", media)