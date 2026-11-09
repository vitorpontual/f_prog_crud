import re

def confirmar_senha():
    while True:
        senha = input("Senha: ")
        confirme_senha = input("Confirme sua senha: ")
        if senha == confirme_senha:
            return senha
            break
        else:
            print("Repita a senha")

def validar_email():
    while True:
        email = input("Email: ")
        
        padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if re.match(padrao, email.strip()):
            return email
            break
        else:
            print("Repita o email")


def calcular_media_estrelas(avaliacoes):
    if len(avaliacoes) == 0:
        return 0.0

    soma = 0
    for av in avaliacoes:
        soma += av['estrelas']

    media = soma / len(avaliacoes)

    return round(media, 1)



