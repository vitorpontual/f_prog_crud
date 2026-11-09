from controller.empresa_controller import *

def menu_empresa_logada(emp):
    cnpj = emp['cnpj']
    while True:
        print(f"\n--- PAINEL DA EMPRESA: {emp['nome']} ---")
        print('1 - Dashboard')
        print('2 - Deletar Conta da Empresa')
        print("0 - Fazer Logout")

        opcao = input("Escolha: ")

        match opcao:
            case '1':
                dash = dashboard(cnpj)
                print(f"\n--- DASHBOARD ---")
                print(f"Total de Avaliações: {dash['total']}")
                print(f"Média Geral: {dash['media']} Estrelas")
                for av in dash['lista']:
                    print(f"[{av['estrelas']} Estrelas]"
                          f"(Email: {av['email']}) - "
                          f"{av['comentario'].capitalize()}")
            case '2':
                confirmacao = input("Tem certeza que quer apagar a conta? [S/N]")
                if confirmacao.upper() == 'S':
                    msg = deletar_conta_empresa(cnpj)
                    print(msg)
                    break
            case '0':
                print("Fazendo logout...")
                break
            case _:
                print("Opção inválida")
