from controller.usuario_controller import *
from views.menu_view import *


while True:
    exibir_menu()

    opc = input("Escolha uma opção: ")
    
    match opc:
        case "1":
            menu_cl()
            opc_lc = int(input(">>>"))
            match opc_lc:
                case 1:
                    cadastro()
                case 2:
                    
                    email = input("Digite seu Email: ")
                    senha = input("Digite sua Senha: ")
                    acesso = login(email, senha)

                    if acesso == False:
                        print(acesso)
                    else:
                        nome = acesso['nome'].split()
                        nome = nome[0] + ' ' + nome[1]
                        menu_usuario(nome.title())
                        opcao = input(input("Escolha uma opção: "))
                
                case _:
                    print("Opção inválida")


        case "2":
            print("implementando...")
        case "0":
            print("Finalizando o Programa")
            break
        case _:
            print("Opção inválida")

if __name__ == "name":
    main()
