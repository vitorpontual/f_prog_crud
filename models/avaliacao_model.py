from utils.database import *
from datetime import datetime
from utils.validacoes import calcular_media_estrelas, sistema_de_selos

FILE = 'avaliacoes.json'
LOG = 'log.json'

def criar_avaliacao(email, cnpj_empresa, nome, estrelas, comentario='', ativa=False):
    avaliacoes = load_json(FILE)
    nova_avaliacao = {
        'empresa': nome,
        'cnpj': cnpj_empresa,
        'email' : email,
        'estrelas' : estrelas,
        'comentario' : comentario,
        'cadastro' : ativa
    }

    avaliacoes.append(nova_avaliacao)
    save_json(FILE, avaliacoes)

def ativar_cadastro_avaliacao(cnpj, ativa="True"):
    avaliacoes = load_json(FILE)
    for av in avaliacoes:
        if av['cnpj'] == cnpj and av['cadastro'] == False:
            av['cadastro'] = True
            
    
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


def buscar_avaliacao_especifica(cnpj):
    avaliacoes = load_json(FILE)
    for avaliacao in avaliacoes:
        if avaliacao['cnpj'] == cnpj:
            return avaliacao

    return None

def update_avaliacao(email, cnpj, estrelas, comentario):
    avaliacoes = load_json(FILE)
    log = load_json(LOG)
    atualizado = False

    for avaliacao in avaliacoes[1:]:
        if avaliacao['email'] == email and avaliacao['cnpj'] == cnpj and avaliacao['cadastro'] == True:
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")

            log_tupla = (data_hora, avaliacao['estrelas'], avaliacao['comentario'], email)
            avaliacao['comentario'] = comentario
            avaliacao['estrelas'] = estrelas
            log.insert(0, {'cnpj': cnpj, 'log': log_tupla})
            atualizado = True

        elif avaliacao['cadastro'] == False:
            avaliacao['comentario'] = comentario
            avaliacao['estrelas'] = estrelas
            atualizado = True
            
    if atualizado:
        save_json(LOG, log)
        save_json(FILE, avaliacoes)
    return atualizado

def deletar_avaliacao(email, cnpj):
    avaliacoes = load_json(FILE)
    lista = []
    log = []

    for av in avaliacoes:
        if av['email'] == email and cnpj == av['cnpj'] and av['cadastro'] == True:
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
            log_tupla = (data_hora, av['estrelas'], av['comentario'], email)
            log.insert(0, {'cnpj': cnpj, 'log': log_tupla})
        elif av['cadastro'] == False:
            pass
        else:
            print(av)
            lista.append(av)

    save_json(LOG, log)
    save_json(FILE, lista)


def deletar_avaliacao_empresa(cnpj):
    avaliacoes = load_json(FILE)
    logs = load_json(LOG)
    lista = []
    log = []

    for av in avaliacoes:
        if cnpj != av['cnpj']:
            lista.append(av)

    for l in logs:
        if cnpj == l['cnpj']:
            log.append(l)

    save_json(LOG, log)
    save_json(FILE, lista)
