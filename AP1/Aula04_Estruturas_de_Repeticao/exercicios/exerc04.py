#Faça um programa para mostrar as tabuadas de todos os números de 1 a 10.


#Com while
multiplicador = 1

while multiplicador <= 10:
    multiplicando = 1
    while multiplicando <=10:
        print(multiplicador, " x ", multiplicando, " = ", multiplicador*multiplicando)
        multiplicando += 1
    
    multiplicador += 1


#Com for
for multiplicador in range(1, 11):
    for multiplicando in range(1, 11):
        print(multiplicador, "x", multiplicando, "=", multiplicando*multiplicando)