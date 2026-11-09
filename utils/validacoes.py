import re
def confirmar_senha():
    senha = ''
    while True:
        senha = input("Digite sua senha: ")
        confirme_senha = input("Confirme sua senha: ")
        if senha == confirme_senha:
            break
        else:
            print("Repita a senha")
    return senha

def validar_email(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(padrao, email.strip()):
        return True
    else:
        return False


def calcular_media_estrelas(avaliacoes):
    if len(avaliacoes) == 0:
        return 0.0

    soma = 0
    for av in avaliacoes:
        soma += av['estrelas']

    media = soma / len(avaliacoes)

    return round(media, 1)
