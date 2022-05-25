import string


def listarTodos(matrizMedicos,matrizPacientes,opcaoSubmenu):
    continuar=True
    while continuar:
        print('=-'*15, 'LISTAR TODOS USUÁRIOS', '=-'*15, '\n')
        if opcaoSubmenu == 1:
            for i in range(len(matrizMedicos)):
                for j in range(len(matrizMedicos[i])):
                    print([matrizMedicos[i][j]], end= " ")
                print('\n')
            retorno=input('Retornar ao menu anterior? (S/N) \n').lower
            if retorno == 's':
                continuar=False
                submenu(matrizMedicos,matrizPacientes,opcaoSubmenu)

        elif opcaoSubmenu == 2:
            for i in range(len(matrizPacientes)):
                for j in range(len(matrizPacientes[i])):
                    print([matrizPacientes[i][j]], end= " ")
                print('\n')
            retorno=input('Retornar ao menu anterior? (S/N) \n').lower
            if retorno == 's':
                continuar=False
                submenu(matrizMedicos,matrizPacientes,opcaoSubmenu)

       
def listarElemento(matrizMedicos,matrizPacientes,opcaoSubmenu):
    continuar=True
    while continuar:
        print('=-'*15, 'LISTAR ELEMENTO', '=-'*15, '\n')

        if opcaoSubmenu==1:

            digito = True

            while digito:
                crm = input("Informe o CRM do médico que deseja listar: ")

                if crm.isdigit is False:
                    print("CRM digitado incorretamente, tente novamente")
                else:

                    encontrou = True

                    while encontrou:
                        for i in range(len(matrizMedicos)):
                            if matrizMedicos[i][0] == crm:
                                for j in range(len(matrizMedicos[i])):
                                    print(matrizMedicos[i][j])
                                    encontrou = False
                    digito = False


            
            '''print("Menus disponíveis",'\n')
            print("0. CRM")
            print("1. Nome")
            print("2. Data de nascimento")
            print("3. Sexo")
            print("4. Especialidade")
            print("5. Universidade")
            print("6. E-mail")
            print("7. Telefone")

            position = int(input("Qual gostaria de ver? \n"))

            for i in range(len(matrizMedicos)):
                print(matrizMedicos[i][position])
                print('\n')
            
            retorno=input('Retornar ao menu anterior? (S/N) \n')
            if retorno == 'S' or retorno == 's':
                continuar=False
                submenu(matrizMedicos,matrizPacientes,opcaoSubmenu)
            else:
                continuar
                print('\n Listar novo elemento \n')

        elif opcaoSubmenu==2:
            print("Menus disponíveis",'\n')
            print("0. CPF")
            print("1. Nome")
            print("2. Data de nascimento")
            print("3. Sexo")
            print("4. Plano de saúde")
            print("5. E-mail")
            print("6. Telefone")

            position = int(input("Qual gostaria de ver? \n"))

            for i in range(len(matrizPacientes)):
                print(matrizPacientes[i][position])
                print('\n')
            
            retorno=input('Retornar ao menu anterior? (S/N) ')
            if retorno == 'S' or retorno == 's':
                continuar=False
                submenu(matrizMedicos,matrizPacientes,opcaoSubmenu)
            else:
                continuar
                print('\n Listar novo elemento \n')'''

def incluir(matrizMedicos,matrizPacientes,opcaoSubmenu):
    continuar=True
    while continuar:
        print('=-'*15, 'ADICIONAR USUÁRIO', '=-'*15, '\n')
        if opcaoSubmenu==1:
            novo_med=[]
            novo_med.append(int(input('Digite o CRM: ')))
            for i in range(len(matrizMedicos)):
                if matrizMedicos[i][0] == novo_med[0]:
                    print('Este usuário já está cadastrado')
                    while matrizMedicos[i][0] == novo_med[0]:
                        novoCRM=(int(input('Digite um CRM válido: ')))
                        novo_med[0]= novoCRM
            nomeletra=True
            while nomeletra:
                nomepac=(input('Digite o nome: '))
                sem_espaco=nomepac.replace(" ","")
                if sem_espaco.isalpha() is True:
                    novo_med.append(nomepac)
                    nomeletra=False
                else:
                    print('Digite caracteres válidos ')
            novo_med.append(input('Digite a data de nascimento: '))
            novo_med.append(str(input('Digite o sexo: ')))
            novo_med.append(str(input('Digite a especialidade: ')))
            novo_med.append(str(input('Digite a universidade: ')))
            novo_med.append(input('Digite o email: '))
            var1=True
            while var1:    
                email=input("adicionar novo email? (S/N)")
                if email== 'N' or email=='n':
                    var1=False
                elif email== 'S' or email=='s':    
                    novo_med.append(str(input('Digite outro email: ')))
                else:
                    print('digite novamente (S/N) ')
            novo_med.append(int(input('Digite outro telefone: ')))
            var2=True
            while var2:    
                tele=input("adicionar novo telefone? (S/N)")
                if tele== 'N' or tele=='n':
                    var2=False
                elif email== 'S' or email=='s':    
                    novo_med.append(int(input('Digite outro telefone: ')))
                else:
                    print('digite novamente (S/N) ')

            matrizMedicos.append(novo_med)

            retorno=input('Retornar ao menu anterior? (S/N) ')
            if retorno == 'S' or retorno == 's':
                continuar=False
                submenu(matrizMedicos,matrizPacientes,opcaoSubmenu)
            else:
                continuar
                print('\n Incluir novo usuário \n')

        elif opcaoSubmenu==2:
            novo_pac=[]
            novo_pac.append(int(input('Digite o CPF: ')))
            for i in range(len(matrizPacientes)):
                if matrizPacientes[i][0] == novo_pac[0]:
                    print('Este usuário já está cadastrado')
                    while matrizPacientes[i][0] == novo_pac[0]:
                        novoCPF=(int(input('Digite um CPF válido: ')))
                        novo_pac[0]= novoCPF
            nomeletra=True
            while nomeletra:
                nomepac=(input('Digite o nome: '))
                sem_espaco=nomepac.replace(" ","")
                if sem_espaco.isalpha() is True:
                    novo_pac.append(nomepac)
                    nomeletra=False
                else:
                    print('Digite caracteres válidos ')
            novo_pac.append(str(input('Digite a data de nascimento: ')))
            novo_pac.append(str(input('Digite o sexo: ')))
            novo_pac.append(str(input('Digite plano de saúde: ')))
            novo_pac.append(str(input('Digite o email: ')))
            var1=True
            while var1:    
                email=input("adicionar novo email? (S/N)")
                if email== 'N' or email=='n':
                    var1=False
                elif email== 'S' or email=='s':    
                    novo_pac.append(str(input('Digite outro email: ')))
                else:
                    print('digite novamente (S/N) ')
            novo_pac.append(int(input('Digite outro telefone: ')))
            var2=True
            while var2:    
                tele=input("adicionar novo telefone? (S/N)")
                if tele== 'N' or tele=='n':
                    var2=False
                elif email== 'S' or email=='s':    
                    novo_pac.append(int(input('Digite outro telefone: ')))
                else:
                    print('digite novamente (S/N) ')

            matrizPacientes.append(novo_pac)

            retorno=input('Retornar ao menu anterior? (S/N) ')
            if retorno == 'S' or retorno == 's':
                continuar=False
                submenu(matrizMedicos,matrizPacientes,opcaoSubmenu)
            else:
                continuar
                print('\n Incluir novo usuário \n')

def alterar(matrizMedicos,matrizPacientes,opcaoSubmenu):
    continuar=True
    while continuar:
        print('=-'*15, 'ALTERAR USUÁRIO', '=-'*15, '\n')
        if opcaoSubmenu==1:
            for i in range(len(matrizMedicos)):
                for j in range(len(matrizMedicos[i])):
                    print(matrizMedicos[i][j], end= " ")
                print('\n')

            print("1. Alterar todos os dados de um usuário")
            print("2. Alterar um dado específico de um usuário")
            print("3. Adicionar dado específico")
            escolha=int(input())
            usuario=int(input("Qual usuário gostaria de alterar? \n"))

            if escolha==1:#alterar completamente um usuário

                for i in range(len(matrizMedicos[usuario])):
                    atualizacao=input('digite o novo dado: ')
                    matrizMedicos[usuario][i]=atualizacao

            elif escolha==2:#alterar info especifica
                info=0
                for i in range(len(matrizMedicos[usuario])):
                    print('\n',info,[matrizMedicos[usuario][i]])
                    info+=1
                dado=int(input('Qual informação gostaria de alterar? '))
                atualizacao=input('digite o novo dado: ')
                for i in range(len(matrizMedicos[usuario])):
                    matrizMedicos[usuario][dado]=atualizacao

            elif escolha==3:#adicionar dado especifico
                info=0
                for i in range(len(matrizMedicos[usuario])):
                    print(info,matrizMedicos[usuario][i])
                    info+=1
                posicao=int(input('Posicao para inserir: '))
                informacao=input('Informação nova: ')
                matrizMedicos[usuario].insert(posicao,informacao)

            print("Alteração realizada com sucesso \n")
            retorno=input('Retornar ao menu anterior? (S/N) ')
            if retorno == 'S' or retorno == 's':
                continuar=False
                submenu(matrizMedicos,matrizPacientes,opcaoSubmenu)
            else:
                continuar
                print('\n Alterar novo usuário \n')
        
        elif opcaoSubmenu==2:
            for i in range(len(matrizPacientes)):
                for j in range(len(matrizPacientes[i])):
                    print(matrizPacientes[i][j], end= " ")
                print('\n')

            print("1. Alterar todos os dados de um usuário")
            print("2. Alterar um dado específico de um usuário")
            print("3. Adicionar dado específico")
            escolha=int(input())
            usuario=int(input("Qual usuário gostaria de alterar? \n"))

            if escolha==1:#alterar completamente um usuário

                for i in range(len(matrizPacientes[usuario])):
                    atualizacao=input('digite o novo dado: ')
                    matrizPacientes[usuario][i]=atualizacao

            elif escolha==2:#alterar info especifica
                info=0
                for i in range(len(matrizPacientes[usuario])):
                    print('\n',info,[matrizPacientes[usuario][i]])
                    info+=1
                dado=int(input('Qual informação gostaria de alterar? '))
                atualizacao=input('digite o novo dado: ')
                for i in range(len(matrizPacientes[usuario])):
                    matrizPacientes[usuario][dado]=atualizacao

            elif escolha==3:#adicionar dado especifico
                info=0
                for i in range(len(matrizMedicos[usuario])):
                    print(info,matrizMedicos[usuario][i])
                    info+=1
                posicao=int(input('Posicao para inserir: '))
                informacao=input('Informação nova: ')
                matrizMedicos[usuario].insert(posicao,informacao)

            print("Alteração realizada com sucesso \n")
            retorno=input('Retornar ao menu anterior? (S/N) ')
            if retorno == 'S' or retorno == 's':
                continuar=False
                submenu(matrizMedicos,matrizPacientes,opcaoSubmenu)
            else:
                continuar
                print('\n Alterar novo usuário \n')
    
def excluir(matrizMedicos,matrizPacientes,opcaoSubmenu):
    continuar=True
    while continuar:
        print('=-'*15, 'EXCLUIR USUÁRIOS', '=-'*15, '\n')
        if opcaoSubmenu==1:
            for i in range(len(matrizMedicos)):
                for j in range(len(matrizMedicos[i])):
                    print([matrizMedicos[i][j]], end= " ")
                print('\n')

            print("1. Excluir todos os dados de um usuário")
            print("2. Excluir um dado específico de um usuário")
            escolha=int(input())
            usuario=int(input("Qual usuário gostaria de exlcuir? \n"))
            if escolha==1:#exlcuir completamente um usuário
                del matrizMedicos[usuario]
            elif escolha==2:#excluir info especifica
                info=0
                for i in range(len(matrizMedicos[usuario])):
                    print('\n',info,[matrizMedicos[usuario][i]])
                    info+=1
                dado=int(input('Qual informação gostaria de ecluir? '))
                del matrizMedicos[usuario][dado]
            print('\n Dados excluídos com sucesso. \n')
            retorno=input('Retornar ao menu anterior? (S/N) ')
            if retorno == 'S' or retorno == 's':
                continuar=False
                submenu(matrizMedicos,matrizPacientes,opcaoSubmenu)
            else:
                continuar
        elif opcaoSubmenu==2:
            for i in range(len(matrizPacientes)):
                for j in range(len(matrizPacientes[i])):
                    print([matrizPacientes[i][j]], end= " ")
                print('\n')
            print("1. Excluir todos os dados de um usuário")
            print("2. Excluir um dado específico de um usuário")
            escolha=int(input())
            usuario=int(input("Qual usuário gostaria de exlcuir? \n"))
            if escolha==1:#exlcuir completamente um usuário
                del matrizPacientes[usuario]
            elif escolha==2:#alterar info especifica
                info=0
                for i in range(len(matrizPacientes[usuario])):
                    print('\n',info,[matrizPacientes[usuario][i]])
                    info+=1
                dado=int(input('Qual informação gostaria de ecluir? '))
                del matrizPacientes[usuario][dado]
            print('\n Dados excluídos com sucesso. \n')
            retorno=input('Retornar ao menu anterior? (S/N) ')
            if retorno == 'S' or retorno == 's':
                continuar=False
                submenu(matrizMedicos,matrizPacientes,opcaoSubmenu)
            else:
                continuar

def submenu(matrizMedicos,matrizPacientes,opcaoSubmenu):
    print('\n', '-='*15, 'SUB MENUS','-='*15, '\n')
    print('1. Listar todos')
    print('2. Listar elemento específico')
    print('3. incluir')
    print('4. alterar')
    print('5. excluir')
    print('6. Voltar ao Menu principal')
    
    operacao = int(input('Digite qual menu gostaria de acessar: \n'))

    if operacao == 1:
        listarTodos(matrizMedicos,matrizPacientes,opcaoSubmenu)
    elif operacao == 2:
        listarElemento(matrizMedicos,matrizPacientes,opcaoSubmenu)
    elif operacao == 3:
        incluir(matrizMedicos,matrizPacientes,opcaoSubmenu)
    elif operacao == 4:
        alterar(matrizMedicos,matrizPacientes,opcaoSubmenu)
    elif operacao == 5:
        excluir(matrizMedicos,matrizPacientes,opcaoSubmenu)
    elif operacao == 6:
        menu_principal(matrizMedicos,matrizPacientes)
    
def menu_principal(matrizMedicos, matrizPacientes):
    print('\n','-='*15,'MENU PRINCIPAL','-='*15,'\n')
    print('1. Médicos')
    print('2. Pacientes')
    print('5. Sair')

    opcaoSubmenu = int(input('Digite qual menu gostaria de acessar: \n'))

    if opcaoSubmenu == 1 or opcaoSubmenu == 2:
        submenu(matrizMedicos,matrizPacientes,opcaoSubmenu)

def main():
    matrizMedicos = [['1245', 'João Pedro', '14/01/1990', 'M', 'Geriatra', 'Unip', 'joaop@google.com', 124578964], ['8962', 'Juliana Pereira', '29/07/1982', 'F', 'Dermatologista', 'UFScar', 'julianap@google.com', 951423687]]
    matrizPacientes = [['12345678920', 'Pedro Coelho', '06/11/2002', 'M', 'Plano Especial 1', 'pedro.coelho@google.com', 114578451],['75314710162', 'Gabriela Santos', '10/05/2000', 'F', 'Plano especial 2', 'gabielaS@google.com', 1154712359 ]]
    menu_principal(matrizMedicos, matrizPacientes)


main()
