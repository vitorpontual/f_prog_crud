from controller.usuario_controller import *
from controller.empresa_controller import *
from views.menu_view import *


while True:
    exibir_menu()

    opt = input("Escolha: ")

    match opt:
        case '1':
            nome = input("Nome: ")
            email = input("Email: ")
            senha = input("Senha: ")
            cpf = input("CPF: ")
            msg = cadastrar_usuario(nome, email, senha, cpf)
            print(msg)
        case '2':
            nome = input("Nome":)
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
