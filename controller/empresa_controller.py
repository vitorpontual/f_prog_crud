from models.empresa_model import *
from models.usuario_model import *
from models.avaliacao_model import *

def cadastrar_empresa(nome, cnpj, senha):
    empresa = buscar_empresa_por_cnpj(cnpj)
    empresa_n = buscar_empresa_por_nome(nome)
    empresa_a = buscar_avaliacao_especifica(cnpj)
    
    try:
        if not empresa and not empresa_a and not empresa_n:
            criar_empresa(nome, cnpj, senha)
            return 'Empresa Cadastrada com sucesso'
        elif empresa and empresa_a or empresa_n and empresa_a:
            porb = empresa['cnpj'] != empresa_a['cnpj'] and empresa_n['nome'] != empresa_a['empresa']
            if porb:
                raise TypeError("Já possui cadastro com o nome ou cnpj")
            else:            
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


