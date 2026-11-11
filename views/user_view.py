from controller.usuario_controller import *
from utils.validacoes import *

def menu_usuario_logado(usuario):
    email = usuario['email']
    cpf = usuario['cpf']
    while True:
        print(f"\n---PAINEL DO USUÁRIO: {usuario['nome']} ---")

        print("1 - Avaliar Empresa (Por CNPJ)")
        print("2 - Alterar Avaliação")
        print("3 - Deletar Avaliação")
        print("4 - Buscar Empresa")
        print("5 - Listar Empresas")
        print("8 - Perfil")
        print("9 - Deletar Minha Conta")
        print("0 - Fazer logout")
        opcao = input("Escolha: ")

        match opcao:
            case '1':
                print("\n---- Avaliar Empresa ----")
                nome = input("Nome da Empresa: ")
                conteudo = "CNPJ da Empresa (pode não estar cadastrada): "
                cnpj = validar_cpf_cnpj(conteudo) 
                try:
                    estrelas = int(input("Nota (0 a 5): "))
                    comentario = input("Comentário (opcional): ")
                    msg = registrar_avaliacao(email, nome, cnpj, estrelas, comentario)
                    print(msg)
                except ValueError:
                    print("Erro: A nota deve ser um número inteiro!")

            case '2':
                cnpj = input("Editar Avaliação da CNPJ da Empresa [CNPJ]: ")
                try: 
                    estrelas = int(input("Nota ( 0 a 5): "))
                    comentario = input("[Editar] Comentário: ")
                    msg = alterar_avaliacao(email, cnpj, estrelas, comentario)
                    print(msg)
                except ValueError:
                    print("Error: A nota de ser um número inteiro!")
            
            case '3':
                print("\n === DELETAR AVALIAÇÃO ===")
                conteudo = "CNPJ: "
                cnpj = validar_cpf_cnpj(conteudo)
                confirmar = input("Deseja excluir a avaliação [S/N]: ")

                if confirmar.upper() == 'S':
                    msg = deletar_avaliacao_usuario(email, cnpj)
                    print(msg)

            case '4':
                print("\n --- BUSCAR EMPRESA ---")
                nome = input("Nome da Empresa: ")
                empresa = buscar_empresa(nome) 
                if empresa[0]:
                    emp = empresa[1]
                    ava = empresa[2]
                    print(f"Nome: {emp['nome'].capitalize()}\nCNPJ: {emp['cnpj']}\nCADASTRADA: {'Sim' if emp['cadastro'] else 'Não'}")
                    print(f"\nAvaliação Total: {ava['total']}\nMédia Estrelas: {ava['media']}")
                    for av in ava['lista']:
                        print(f"\nComentário: {av['comentario']}")
                        print(f"Estrela: {av['estrelas']}")
                        print(f"Autor: {av['email']}")
                else:
                    print(empresa[1])


            case '5':
                print("\n --- LISTA DAS EMPRESAS E AVALIAÇÕES ---")
                empresas = listar_empresas()
                for emp in empresas:
                    print(f"Nome da Empresa: {emp['nome'].title()}")
                    print(f"CNPJ da Empresa: {emp['cnpj']}")


            case '8':
                print(f"\n --- PERFIL {usuario['nome']} ----")
                perfil = perfil_usuario(usuario['email'])

                print(f"\nNOME: {usuario['nome']}")
                print(f"EMAIL: {usuario['email']}")
                if usuario['pcd']:
                    print(f"DEFICIÊNCIA: {usuario['pcd']}")

            case '9':
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
