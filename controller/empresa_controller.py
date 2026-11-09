from models.empresa_model import *
from models.usuario_model import *
from models.avaliacao_model import *
from utils.validacoes import *

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

def dashboard(cnpj):
    avaliacoes = buscar_avaliacoes_por_empresa(cnpj)
    media = calcular_media_estrelas(avaliacoes)
    lista_dashboard = []

    for av in avaliacoes:
        usuario = buscar_usuario_por_email(av['email'])

        email = usuario['email'] if usuario else "Usuário não existe!"
        lista_dashboard.append({
            'estrelas': av['estrelas'],
            'comentario': av['comentario'],
            'email': email
        })

    return {
        'total': len(avaliacoes),
        'media_estrelas': media,
        'lista': lista_dashboard
    }
  
def deletar_conta_empresa(cnpj):
    deletar_empresa_por_cnpj(cnpj)
    return "Conta deletada com sucesso!"
