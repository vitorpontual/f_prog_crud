from controller.usuario_controller import *
from utils.validacoes import *

def menu_usuario_logado(usuario):
    email = usuario['email']
    cpf = usuario['cpf']
    while True:
        print(f"\n---PAINEL DO USUÁRIO: {usuario['nome']} ---")

        print("1 - Avaliar Empresa (Por CNPJ)")
        print("2 - Alterar Avaliação")
        print("3 - Ver Empresas e suas Avaliações")
        print("4 - Deletar Minha Conta")
        print("0 - Fazer logout")
        opcao = input("Escolha: ")

        match opcao:
            case '1':
                cnpj = input("CNPJ da Empresa (pode não estar cadastrada): ")
                try:
                    estrelas = int(input("Nota (0 a 5): "))
                    comentario = input("Comentário (opcional): ")
                    msg = registrar_avaliacao(email, cnpj, estrelas, comentario)
                    print(msg)
                except ValueError:
                    print("Erro: A nota deve ser um número inteiro!")
            case '2':
                cnpj = input("CNPJ da Empresa avaliada: ")
                try: 
                    estrelas = int(input("Nota ( 0 a 5): "))
                    comentario = input("[Editar] Comentário: ")
                    msg = alterar_avaliacao(email, cnpj, estrelas, comentario)
                    print(msg)
                except ValueError:
                    print("Error: A nota de ser um número inteiro!")
            
            case '3':
                dados = listar_empresas()
                print("\n --- TODAS EMPRESAS E AVALIAÇÕES ---")
                for item in dados:
                    print(f"\nEmpresa: {item['empresa']}")
                    print(f"CNPJ: {item['cnpj']}")
                    print(f"Média Geral -> {item['media']}")
                    if not item['avaliacoes']:
                        print("\t-> Nenhuma avaliação ainda.")
                    else:
                        for av in item['avaliacoes']:
                            print(f"\t->[{av['estrelas']}]->[{av['comentario']}] de [{av['email']}]")
                    print("-"*50)

            case '4':
                confirmacao = input("Tem certeza que deseja deletar sua conta? [S/N]")
                if confirmacao.upper() == "S":
                    msg = deletar_conta_usuario(cpf)
                    print(msg)
                    break
                    
            case '0':
                print("Fazendo logout... ")
                break
            case _:
                print("Opção inválida")
