#Faça um programa que receba a idade de um eleitor e informa se o
#voto dele é facultativo (entre 16 e 17 anos), obrigatório (entre 18 a 65),
#se ele está dispensado de votar (acima de 65) ou ainda se ele não tem
#idade para votar.


idade = int(input("Digite a sua idade:"))

if idade == 16 or idade == 17:
    print("Seu voto é facultativo")
elif idade >= 18 and idade <= 65:
    print("Seu voto é obrigatório")
elif idade > 65:
    print("Você está dispensado de votar")
else:
    print("Você não tem idade para votar")