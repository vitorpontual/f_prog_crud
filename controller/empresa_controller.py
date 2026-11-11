from models.empresa_model import *
from models.usuario_model import *
from models.avaliacao_model import *

def cadastrar_empresa(nome, cnpj, senha):
    empresa = buscar_empresa_por_cnpj(cnpj)
    if empresa:
        if empresa['cadastro'] == True:
            return "Error: Já existe uma empresa com este CNPJ."
        else:
            ativar_cadastro_empresa(nome, cnpj, senha)
            return 'Cadastro Efetivado com Sucesso! Sua empresa já possuia avalaiações prévias'

    criar_empresa(nome, cnpj, senha)
    return "Empresa cadastrada com sucesso!"


def empresa_login(cnpj, senha):
    empresa = buscar_empresa_por_cnpj(cnpj)
    if empresa and empresa['senha'] == senha and empresa['cadastro'] == True:
        return empresa
    return None

def dashboard(cnpj):
    avaliacoes = buscar_avaliacoes_por_empresa(cnpj)

    if not avaliacoes:
        print("\nA Empresa não foi avaliada!")
        return False

    return avaliacoes
      
def obter_log(cnpj):
    log = buscar_log(cnpj) 
    if not log:
        print("\nHistórico Vazio")
        return False
  
    return log


def deletar_conta_empresa(cnpj):
    deletar_empresa_por_cnpj(cnpj)
    return "Conta deletada com sucesso!"
