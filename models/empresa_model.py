from utils.database import *

FILE = 'empresa.json'

def criar_empresa(nome, cnpj, senha):
    empresas = load_json(FILE)
    nova_empresa = {
        'nome': nome, 'cnpj': cnpj, "senha": senha
    }
    empresas.append(nova_empresa)
    save_json(FILE, empresas)

def buscar_empresa_por_cnpj(cnpj):
    empresas = load_json(FILE)
    for empresa in empresas:
        if empresa['cnpj'] == cnpj:
            return empresa
    return None
