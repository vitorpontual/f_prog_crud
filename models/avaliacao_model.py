from utils.database import *
from datetime import datetime
from utils.validacoes import calcular_media_estrelas

FILE = 'avaliacoes.json'
LOG = 'log.csv'

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
            lista.append({
                'estrelas': avaliacao['estrelas'],
                'comentario': avaliacao['comentario'],
                'email': avaliacao['email']
            })
    media = calcular_media_estrelas(lista)
   
    if not lista:
        return []
    else:
        return {
            'total': len(lista),
            'media': media,
            'lista': lista
        }

def buscar_log(cnpj):
    historico = load_json(LOG)
    lista = []
    for log in historico:
        if log['cnpj'] == cnpj:
            tupla = tuple(log['log'])

            lista.append(tupla)

    return lista


def buscar_avaliacao_especifica(email, cnpj):
    avaliacoes = load_json(FILE)
    for avaliacao in avaliacoes:
        if avaliacao['email'] == email and avaliacao['cnpj'] == cnpj:
            return avaliacao

    return None


def update_avaliacao(email, cnpj, estrelas, comentario):
    avaliacoes = load_json(FILE)
    log = load_json(LOG)
    atualizado = False

    for avaliacao in avaliacoes:
        if avaliacao['email'] == email and avaliacao['cnpj'] == cnpj:
            data_hora = datetime.now().strftime("%Y/%m/%d %H:%M")

            log_tupla = (data_hora, avaliacao['estrelas'], avaliacao['comentario'], email)
            avaliacao['comentario'] = comentario
            avaliacao['estrelas'] = estrelas
            log.append({'cnpj': cnpj, 'log': log_tupla})
            atualizado = True
            break
            

    if atualizado:
        save_json(LOG, log)
        save_json(FILE, avaliacoes)
    return atualizado

def deletar_avaliacao(email, cnpj):
    avaliacoes = load_json(FILE)
    lista = []
    lixo = []

    for av in avaliacoes:
        if av['email'] == email and cnpj == av['cnpj']:
            lixo.append(av)
        else:
            lista.append(av)

    save_json(FILE, lista)

