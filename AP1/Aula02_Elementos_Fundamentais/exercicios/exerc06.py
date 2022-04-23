#Faça um programa que receba o salário de um funcionário, reajusta o salário em 25% e apresenta 
#o valor do reajuste e o novo salário após o aumento.

salarioAntigo = float(input("Informe o salário atual: "))

salarioNovo = (salarioAntigo * 0.25) + salarioAntigo

print("O salário novo é: ", salarioNovo)