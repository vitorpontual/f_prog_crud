from models.empresa_model import *
from models.usuario_model import *
from models.avaliacao_model import *

def cadastrar_empresa(nome, cnpj, senha):
    empresa = buscar_empresa_por_cnpj(cnpj)
    empresa_a = buscar_avaliacao_especifica(cnpj)
    try:
        if not empresa and empresa_a['cnpj'] != cnpj and empresa_a['empresa'] != nome:
            criar_empresa(nome, cnpj, senha)
            return 'Empresa Cadastrada com sucesso'
        elif empresa:
            if empresa['cnpj'] == cnpj and empresa_a['empresa'] == nome and empresa['cadastro'] == False:
                ativar_cadastro_empresa(nome, cnpj, senha)
                ativar_cadastro_avaliacao(cnpj)

                return 'Cadastro Efetivado com Sucesso! Sua empresa já possuia avalaiações prévias'


        raise ValueError("Erro ao cadastrar a empresa! Já existe um empresa com CNPJ ou Nome Predefinido")
    except Exception as e:
        print(e)

    


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
    deletar_avaliacao_empresa(cnpj)
    return "Conta deletada com sucesso!"


