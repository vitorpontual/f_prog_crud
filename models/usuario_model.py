from utils.database import *


FILE = 'usuario.json'

def criar_usuario(nome, email, senha, cpf, pcd=''):
    usuarios = load_json(FILE)
    if pcd:
        novo_usuario = {
            'nome': nome, 'email': email, 'senha': senha, 'cpf': cpf, 'pcd': pcd
        }
    else:
        novo_usuario = {
            'nome': nome, 'email': email, 'senha': senha, 'cpf': cpf, 'pcd': pcd
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

def deletar_usuario_por_cpf(cpf):
    usuarios = load_json(FILE)
    
    lista = []

    for usuario in usuarios:
        if usuario['cpf'] != cpf:
            lista.append(usuario)

    save_json(FILE, lista)
