from utils.database import *

FILE = 'avalaliacao.json'

def criar_avaliacao(email, cnpj_empresa, estrelas, comentario='', ativa=False):
    avaliacoes = load_json(FILE)
    nova_avaliacao = {
        'email' : email,
        'cnpj': cnpj_empresa,
        'estrelas' : estrelas,
        'comentario' : comentario }

    avaliacoes.append(nova_avaliacao)
    save_json(FILE, avaliacoes)


def buscar_avaliacoes_por_empresa(cnpj):
    avaliacoes = load_json(FILE)
    lista = []
    for avaliacao in avaliacoes:
        if avaliacao['cnpj'] == cnpj:
            lista.append(avaliacao)

    return lista


def buscar_avaliacao_especifica(email, cnpj):
    avaliacoes = load_json(FILE)
    for avaliacao in avaliacoes:
        if avaliacao['email'] == email and avaliacao['cnpj'] == cnpj:
            return avaliacao

    return None


def update_avaliacao(email, cnpj, estrelas, comentario):
    avaliacoes = load_json(FILE)
    atualizado = False

    for avaliacao in avaliacoes:
        if avaliacao['email'] == email and avaliacao['cnpj'] == cnpj:
            avaliacao['comentario'] = comentario
            avaliacao['estrelas'] = estrelas
            atualizado = True
            break

    if atualizado:
        save_json(FILE, avaliacoes)
    return atualizado

def deletar_avaliacao(email, cnpj):
    avaliacoes = load_json(FILE)
    lista = []

    for av in avaliacoes:
        if av['email'] != email and cnpj == av['cnpj']:
            lista.append(av)

    save_json(FILE, lista)

