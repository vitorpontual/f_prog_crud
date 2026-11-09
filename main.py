from controller.usuario_controller import *
from controller.empresa_controller import *
from views.main_menu import *
from views.empresa_view import *
from views.user_view import *

while True:
    main_menu()

    opt = input("Escolha: ")

    match opt:
        case '1':
            email = input("Email: ")
            senha = input("Senha: ")
            usuario = usuario_login(email, senha)
            if usuario:
                print("Login realizado com sucesso!")
                menu_usuario_logado(usuario)
            else:
                print("Erro: Email ou senha incorretos.")
        case '2':
            cnpj = input("CNPJ: ")
            senha = input("Senha: ")
            empresa = empresa_login(cnpj, senha)
            if empresa:
                print("Login realizado com sucesso!")
                menu_empresa_logada(empresa)
            else:
                print("Erro: CNPJ ou senha incorretos.")
            
        case '3':
            nome = input("Nome: ")
            email = input("Email: ")
            senha = input("Senha: ")
            cpf = input("CPF: ")
            msg = cadastrar_usuario(nome, email, senha, cpf)
            print(msg)
        case '4':
            nome = input("Nome: ")
            cnpj = input("CNPJ: ")
            senha = input("Senha: ")
            msg = cadastrar_empresa(nome, cnpj, senha)
            print(msg)

        case '0':
            print("Sistema encerrado.")
            break
        case _ :
            print("Opção inválida")

    




if __name__ == 'name':
    main()
