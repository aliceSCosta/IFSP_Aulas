#Faça um programa que leia 2 notas de um aluno, onde a primeira nota possui peso um, a segunda possui peso dois. Calcule a média
#ponderada do aluno baseada nos pesos e exiba.

print("---- Calculadora média ponderada ----")

nota1 = int(input("Informe a primeira nota: "))
nota2 = int(input("Informe a segunda nota: "))

media = nota1*1 + nota2*2 / 3

print("A média do aluno é: ", media)