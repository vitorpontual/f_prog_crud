from models.empresa_model import *

def cadastrar_empresa(nome, cnpj, senha):
    if buscar_empresa_por_cnpj(cnpj):
        return "Error: Já existe uma empresa com este CNPJ."

    criar_empresa(nome, cnpj, senha)
    return "Empresa cadastrada com sucesso!"


def empresa_login(cnpj, senha):
    empresa = buscar_empresa_por_cnpj(cnpj)
    if empresa and empresa['senha'] == senha:
        return empresa
    return None
