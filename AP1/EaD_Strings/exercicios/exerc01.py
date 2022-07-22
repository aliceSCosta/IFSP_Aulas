palavra = input("Informe uma string: ")
letra = input("Digite a letra que deseja remover: ")


contador = 0
for i in palavra:
    if i == letra and contador == 0 :
        palavra = palavra.replace(i,"")
        contador = 1
print(palavra)