'''Faça um programa que receba um número inteiro maior que 1,
verifique se o número é primo ou não e mostre a mensagem de
número primo ou de número não primo. Obs: Um número é primo
quando é divisível apenas por 1 e por ele mesmo.'''


dividendo = int(input("Escolha um número: "))

divisores = 0

#Com while
if dividendo > 1:
    
    divisor = 0
    while divisor < dividendo:
        divisor+=1
        if dividendo%divisor == 0:
            divisores +=1

    if divisores == 2:
        print("O número é primo")
    else:
        print(f'O número não é primo e tem {divisores} divisores')
else:
    print('Digite um número maior que 1!')



#Com for
if dividendo > 1:
    for divisor in range (1, dividendo+1):
        if dividendo%divisor == 0:
            divisores += 1

    if divisores == 2:
        print("O número é primo")
    else:
        print(f"O número não é primo e tem {divisores} divisores")
else:
    print("Digite um número maior que 1!")