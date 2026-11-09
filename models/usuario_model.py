from utils.database import *


FILE = 'usuarios.json'

def criar_usuario(nome, email, senha, cpf):
    usuarios = load_json(FILE)
    novo_usuario = {
        'nome': nome, 'email': email, 'senha': senha, 'cpf': cpf
    }
    usuarios.append(novo_usuario)
    save_json(FILE, usuarios)

def buscar_usuario_por_cpf(cpf):
    usuarios = load_json(FILE)
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario
    return None

def buscar_usuario_por_email(email):
    usuarios = load_json(FILE)
    for usuario in usuarios:
        if usuario['email'] == email:
            return usuario
    return None
