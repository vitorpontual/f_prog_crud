from models.usuario_model import *
from models.avaliacao_model import *
from models.empresa_model import *
from utils.validacoes import *

def cadastrar_usuario(nome, email, senha, cpf, pcd):
    if buscar_usuario_por_cpf(cpf):
        return "Error: Já existe um usuário cadastrado com esse CPF."

    if buscar_usuario_por_email(email):
        return "Error: Já existe um usuário cadastrado com esse Email"

    
    criar_usuario(nome, email, senha, cpf, pcd)
    return 'Usuário cadastrado com sucesso'


def usuario_login(email, senha):
    usuario = buscar_usuario_por_email(email)

    if usuario and usuario['senha'] == senha:
        return usuario
    return None

def registrar_avaliacao(email, nome, cnpj, estrelas, comentario):
    if not (0 <= estrelas <= 5):
        return "Erro: A nota deve ser entre 0 e 5 estrelas"

    if buscar_avaliacao_especifica(email, cnpj):
        return "Erro: Você já avaliou a empresa. Use a opção alterar comentário se desejar."

    empresa = buscar_empresa_por_cnpj(cnpj)
    if not empresa:
        criar_empresa(nome, cnpj,"",False)
        
    criar_avaliacao(email, cnpj, estrelas, comentario)
    return 'Avaliação Registrada com suceso!'

def perfil_usuario(email):
    usuario = buscar_usuario_por_email(email)

    return usuario



def alterar_avaliacao(email, cnpj, estrelas, comentario):
    avaliacao = buscar_avaliacao_especifica(email, cnpj)

    if not avaliacao:
        return "Error: Você ainda não avaliou está empresa."

    sucesso = update_avaliacao(email, cnpj, estrelas, comentario)
    if sucesso:
        return 'Avalaiação alterada com sucesso!'
    return "Error ao atualizar"

def buscar_empresa(nome):
    empresa = buscar_empresa_por_nome(nome)   
    if not empresa:
        return (False,'Empresa não encontrada')

    avaliacao = buscar_avaliacoes_por_empresa(empresa['cnpj'])

    if not avaliacao:
        return (False, f'{empresa['nome'].capitalize()} sem avalaiaçõs')
    
    return (True, empresa, avaliacao)

def listar_empresas():
    empresas = listar_todas_empresas()

    if not empresas:
        return 'Nenhuma empresas cadastrada'


    return empresas

def deletar_conta_usuario(cpf):
    deletar_usuario_por_cpf(cpf)
    return "Conta deletada com sucesso."

def deletar_avaliacao_usuario(email, cnpj):
    
    deletar = deletar_avaliacao(email,cnpj)
    if not deletar:
        return "Empresa não cadastrada"

    return "Avaliacação deletada com sucesso."


