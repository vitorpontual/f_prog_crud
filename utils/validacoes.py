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

def validar_cpf_cnpj(conteudo):
    while True:
        try:
            cpf_cnpj = input(f"{conteudo}")

            if cpf_cnpj.isdigit():
                return cpf_cnpj
            else:
                raise ValueError("CPF/CNPJ Inválido")
        except Exception as e:
            print(e)


def cpf_validador_real():
    while True:
        try:
            cpf_entrada = input("CPF: ")

            cpf = ''.join(cha for cha in cpf_entrada if cha.isdigit())


            if len(cpf) != 11 or cpf == cpf[0] * 11:
                raise ValueError("CPF Inválido")

            soma_1 = 0
            peso_1 = 10
            soma_2 = 0
            peso_2 = 11

            for i in range(9):
                soma_1 += int(cpf[i]) * peso_1
                peso_1 -= 1

            resto_1 = (soma_1 * 10) % 11
            d1 = 0 if resto_1 in (10, 11) else resto_1

            for i in range(10):
                soma_2 += int(cpf[i]) * peso_2 
                peso_2 -= 1

            resto_2 = (soma_2 * 10) % 11
            d2 = 0 if resto_2 in (10,11) else resto_2

            if int(cpf[9]) == d1 and int(cpf[10]) == d2:
                return cpf
            else:
                raise ValueError("Digito incorreto")
        except Exception as e:
            print(e)
        else:
            break



