from models.usuario_model import *
from models.avaliacao_model import *
from models.empresa_model import *

def cadastrar_usuario(nome, email, senha, cpf):
    if buscar_usuario_por_cpf(cpf):
        return "Error: Já existe um usuário cadastrado com esse CPF."

    if buscar_usuario_por_email(email):
        return "Error: Já existe um usuário cadastrado com esse Email"

    
    criar_usuario(nome, email, senha, cpf)
    return 'Usuário cadastrado com sucesso'


def usuario_login(email, senha):
    usuario = buscar_usuario_por_email(email)

    if usuario and usuario['senha'] == senha:
        return usuario
    return None

def registrar_avaliacao(email, cnpj, estrelas, comentario):
    if not (0 <= estrelas <= 5):
        return "Erro: A nota deve ser entre 0 e 5 estrelas"

    if buscar_avaliacao_especifica(email, cnpj):
        return "Erro: Você já avaliou a empresa. Use a opção alterar comentário se desejar."
    criar_avaliacao(email, cnpj, estrelas, comentario)
    return 'Avaliação Registrada com suceso!'



def alterar_avaliacao(email, cnpj, estrelas, comentario):
    avaliacao = buscar_avaliacao_especifica(email, cnpj)

    if not avaliacao:
        return "Error: Você ainda não avaliou está empresa."

    sucesso = update_avaliacao(email, cnpj, estrelas, comentario)
    if sucesso:
        return 'Avalaiação alterada com sucesso!'
    return "Error ao atualizar"


def listar_empresas():
    empresas = listar_empresas()

    lista_completa = []

    for emp in empresas:
        avaliacoes = buscar_avaliacoes_por_empresa(emp)

    lista_completa.append({
        'empresa': emp['nome'],
        'cnpj': emp['cnpj'],
        'avaliacoes': avaliacoes
    })

    return lista_completa

def deletar_conta_usuario(cpf):
    deletar_usuario_por_cpf(cpf)
    return "Conta deletada com sucesso."


