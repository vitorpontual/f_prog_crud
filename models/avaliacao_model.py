from utils.database import *

FILE = 'avalaliacao.json'

def criar_avaliacao(cpf_usuario, cnpj_empresa, estrelas, comentario=''):
    avaliacoes = load_json(FILE)
    nova_avaliacao = {
        'cpf_usuario' : cpf_usuario,
        'cnpj_empresa': cnpj_empresa,
        'estrelas' : estrelas,
        'comentario' : comentario }

    avaliacoes.append(nova_avaliacao)
    save_json(FILE, avaliacoes)


def buscar_avaliacoes_por_empresa(cnpj):
    avaliacaoes = load_json(FILE)
    for avaliacao in avaliacoes:
        if avalaliacao['cnpj'] == cnpj:
            return avaliacao


def buscar_avaliacao_especifica(cpf, cnpj):
    avaliacoes = load_json(FILE)
    for avaliacao in avaliacoes:
        if avaliacao['cpf'] == cpf and avaliaca['cnpj'] == cnpj:
            return avaliacao

    return None
