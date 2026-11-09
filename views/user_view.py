from controller.usuario_controller import *
def menu_usuario_logado(usuario):
    cpf = usuario['cpf']
    while True:
        print(f"\n---PAINEL DO USUÁRIO: {usuario['nome']} ---")

        print("1 - Avaliar Empresa (Por CNPJ)")
        print("0 - Fazer logout")
        opcao = input("Escolha: ")

        match opcao:
            case '1':
                cnpj = input("CNPJ da Empresa (pode não estar cadastrada): ")
                try:
                    estrelas = int(input("Nota (0 a 5): "))
                    comentario = input("Comentário (opcional): ")
                    msg = registrar_avaliacao(cpf, cnpj, estrelas, comentario)
                except ValueError:
                    print("Erro: A nota deve ser um número inteiro!")
            case '0':
                print("Fazendo logout... ")
                break
            case _:
                print("Opção inválida")
