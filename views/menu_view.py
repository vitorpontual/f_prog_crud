def exibir_menu():
    print("\n ===== Bem vindo ao Elo Acéssivel ====")

    print("1 - Usuário")
    print("2 - Empresa")
    print("0 - Sair")


def menu_cl():
    print("\n ==== Cadastrar/ Login ====")

    print("1 - Cadastro")
    print("2 - Login")
    


def menu_usuario(nome):
    print(f"\n ==== Bem-vindo {nome} ====")

    print("1 - Cadastrar Avaliação")
    print("2 - Buscar Empresa")
    print("3 - Listar Empresas Cadastradas")
    print("4 - Alterar Avaliação")
    print("5 - Deletar Avaliação")


def menu_empresa(nome):
    print(f"\n ==== Bem-vindo {nome} ====")

    print("1 - Visualizar Avaliação")
    print("2 - Saldo de usuários")
    print("3 - Plano Atual")
