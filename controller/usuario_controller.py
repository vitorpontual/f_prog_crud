from models.usuario_model import *


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
