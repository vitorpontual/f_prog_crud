from utils.database import *

FILE = 'empresa.json'

def criar_empresa(nome, cnpj, senha, cadastro=True):
    empresas = load_json(FILE)
    nova_empresa = {
        'nome': nome.lower().strip(), 'cnpj': cnpj, "senha": senha, "cadastro": cadastro
    }
    empresas.append(nova_empresa)
    save_json(FILE, empresas)

def ativar_cadastro_empresa(nome_real, cnpj, senha):
    empresas = load_json(FILE)
    for emp in empresas:
        if emp['cnpj'] == cnpj:
            emp['nome'] = nome_real
            emp['senha'] = senha
            emp['cadastro'] = True
            break
        
    save_json(FILE, empresas)

def buscar_empresa_por_cnpj(cnpj):
    empresas = load_json(FILE)
    for empresa in empresas:
        if empresa['cnpj'] == cnpj:
            return empresa
    return None

def buscar_empresa_por_nome(nome):
    empresas = load_json(FILE)

    for empresa in empresas:
        if empresa['nome'] == nome.lower():
            return empresa
    return None

def listar_todas_empresas():
    empresas = load_json(FILE)
    lista = []
    if not empresas:
        return "Nenhuma Empresa Cadastrada Ainda."

    
    for emp in empresas:
        lista.append(emp)

    return lista[1:]
        
    

def deletar_empresa_por_cnpj(cnpj):
    empresas = load_json(FILE)
    
    lista = []
    for emp in empresas:
        if emp['cnpj'] != cnpj:
            lista.append(emp)

    save_json(FILE, lista)

    
    
