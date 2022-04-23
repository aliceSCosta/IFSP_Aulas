#Uma determinada loja está fazendo promoções de vendas. Qualquer
#compra que um cliente fizer até R$ 100,00 receberá 5% de desconto. Se
#a compra for maior que R$ 100,00, mas inferior a R$ 200,00, o desconto
#será de 10%. Se for superior ou igual a R$ 200,00, o desconto será de
#20%.
#Faça um programa que leia o quanto o cliente gastou e escreva o valor da
#conta já com os descontos.


valorGasto = float(input("Entre com o valor total gasto: "))

if valorGasto > 100 and valorGasto < 200:
    print("Valorde com desconto: ", valorGasto * 0.9)
elif valorGasto >= 200:
    print("Valor com desconto: ", valorGasto * 0.8)
else:
    print("Valor com desconto: ", valorGasto * 0.95)