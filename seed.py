import os
from utils.database import save_json

def rodar_seed():
    # Cria a pasta database se ela não existir
    if not os.path.exists('database'):
        os.makedirs('database')

    print("🌱 Plantando a semente (populando o banco)...")

    # 1. Povoando Usuários
    usuarios_iniciais = [
        {"nome": "Vitor Guedes", "email": "vitor@email.com", "senha": "123", "cpf": "111"},
        {"nome": "João Silva", "email": "joao@email.com", "senha": "123", "cpf": "222"},
        {"nome": "Maria Costa", "email": "maria@email.com", "senha": "123", "cpf": "333"}
    ]
    # Ajuste o nome do arquivo conforme a sua constante FILE ou caminho exato
    save_json('usuario.json', usuarios_iniciais) 

    # 2. Povoando Empresas
    empresas_iniciais = [
        {"nome": "Mercado Livre", "cnpj": "1010", "senha": "123", "cadastro": True},
        {"nome": "CESAR School", "cnpj": "2020", "senha": "123", "cadastro": True},
        {"nome": "Empresa Não Cadastrada", "cnpj": "9999", "senha": "", "cadastro": False}
    ]
    save_json('empresa.json', empresas_iniciais)

    # 3. Povoando Avaliações
    # ATENÇÃO: Use as chaves exatas que você definiu no seu avaliacao_model.py ('cnpj')
    avaliacoes_iniciais = [
        {
            "email": "vitor@email.com", 
            "cnpj": "1010", 
            "estrelas": 1, 
            "comentario": "Entrega Demora muito!",
        },
        {
            "email": "joao@email.com", 
            "cnpj": "1010", 
            "estrelas": 4, 
            "comentario": "Muito bom, mas a caixa veio amassada.",
            "historico": [
                ("10/11/2026 10:00", "Caixa toda destruída, odiei.") # Exemplo de histórico já pronto!
            ]
        },
        {
            "email": "maria@email.com", 
            "cnpj": "9999", 
            "estrelas": 1, 
            "comentario": "Serviço péssimo, por isso nem cadastro têm.",
        }
    ]
    save_json('avaliacoes.json', avaliacoes_iniciais)

    logs_iniciais = [
    {
            "cnpj": "1010",
            "log": [
                "2026/11/11 14:43",
                5,
                "Entrega super rápida!",
                "vitor@email.com"
            ]
        }

    ]

    print("✅ Banco de dados populado com sucesso! Já pode testar.")

if __name__ == "__main__":
    rodar_seed()
