import json
import os
from utils.validacoes import *

db = "database/usuario.json"

def carregar_usuarios():
    if not os.path.exists(db):
        print("Banco de dados não encontrado. Criando um novo arquivo...")
        with open(db, 'w', encoding='utf-8') as f:
            json.dump([], f)
        return [] # Retorna a lista vazia

    # 2. Se o arquivo existe, lê e carrega os dados normalmente
    with open(db, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            # Caso o arquivo exista mas esteja totalmente em branco (limpo incorretamente)
            return []

def cadastro():
    usuarios = carregar_usuarios()

    nome = input("Digte seu Nome Completo: ").lower()
    email = ''
    while True:
        email = input("Digite seu email: ").lower()
        if validar_email(email):
            if email in usuarios:
                print("Email já cadastrado")
            else:
                break
        else:
            print("Digite um email válido")

    senha = confirmar_senha()

    usuario = {email: {
        'nome': nome,
        'senha': senha
    }}


    try:
        with open(db,'w', encoding="utf-8") as f:
            json.dump(usuario, f, indent=2)

    except json.JSONDecodeError:
        return []

def login(email, senha):
    usuarios = carregar_usuarios()
    
    if email in usuarios and senha == usuarios[email]['senha']:
        return usuarios[email]
    else:
        print("Email ou senha Inválida")
        return False



def perfil(email):
    usuarios = carregar_usuarios()

    if email in usuarios:
        print(email)



    

