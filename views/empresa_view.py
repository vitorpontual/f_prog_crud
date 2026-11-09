def menu_empresa_logada(emp):
    while True:
        print(f"\n--- PAINEL DA EMPRESA: {emp['nome']} ---")
        print("0 - Fazer Logout")

        opcao = input("Escolha: ")

        match opcao:
            case '0':
                print("Fazendo logout...")
                break
            case _:
                print("Opção inválida")
