from utils.database import *
from datetime import datetime
from utils.validacoes import calcular_media_estrelas, sistema_de_selos

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
            'selo' : sistema_de_selos(len(lista), media),
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
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")

            log_tupla = (data_hora, avaliacao['estrelas'], avaliacao['comentario'], email)
            avaliacao['comentario'] = comentario
            avaliacao['estrelas'] = estrelas
            log.insert(0, {'cnpj': cnpj, 'log': log_tupla})
            atualizado = True
            break
            
    if atualizado:
        save_json(LOG, log)
        save_json(FILE, avaliacoes)
    return atualizado

def deletar_avaliacao(email, cnpj):
    avaliacoes = load_json(FILE)
    lista = []
    log = []

    for av in avaliacoes:
        if av['email'] == email and cnpj == av['cnpj']:
            data_hora = datetime.now().strftime("%d/%m/%Y% %H:%M")
            log_tupla = (data_hora, av['estrelas'], av['comentario'], email)
            log.insert(0, {'cnpj': cnpj, 'log': log_tupla})
        else:
            print(av)
            lista.append(av)

    save_json(LOG, log)
    save_json(FILE, lista)
    return lista

