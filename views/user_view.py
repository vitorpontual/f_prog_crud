def menu_usuario_logado(usuario):
    while True:
        print(f"\n---PAINEL DO USUÁRIO: {usuario['nome']} ---")

        print("0 - Fazer logout")
        opcao = input("Escolha: ")

        match opcao:
            case '0':
                print("Fazendo logout... ")
                break
            case _:
                print("Opção inválida")
