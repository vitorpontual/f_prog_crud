from models.usuario_model import *
from models.avaliacao_model import *

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

def registrar_avaliacao(cpf, cnpj, estrelas, comentario):
    if not (0 <= estrelas <= 5):
        return "Erro: A nota deve ser entre 0 e 5 estrelas"

    if buscar_avaliacao_especifica(cpf, cnpj):
        return "Erro: Você já avaliou a empresa. Use a opção alterar comentário se desejar."
    criar_avaliacao(cpf, cnpj, estrelas, comentario)
    return 'Avaliação Registrada com suceso!'
