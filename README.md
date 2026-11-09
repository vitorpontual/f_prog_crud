# 📊 Sistema de Avaliações de Empresas (CRUD em Python)

Um sistema completo de linha de comando (CLI) desenvolvido em **Python Puro**, sem o uso de bibliotecas externas ou orientação a objetos (sem classes), focado em programação funcional e no padrão de arquitetura **MVC (Model-View-Controller)**. 

Os dados são armazenados localmente utilizando arquivos `.json`.

## ✨ Funcionalidades

### 👤 Usuários
* **Cadastro e Login:** Validação de unicidade de CPF e E-mail para evitar cadastros duplicados.
* **Avaliação de Empresas:** Permite avaliar empresas (de 0 a 5 estrelas e comentário) informando apenas o CNPJ. *A empresa não precisa estar cadastrada no sistema para receber uma avaliação.*
* **Edição de Avaliações:** O usuário pode alterar o comentário de avaliações passadas.
* **Listagem:** Visualização de todas as empresas cadastradas e suas respectivas avaliações.
* **Exclusão de Conta:** Deleção completa da conta de usuário.

### 🏢 Empresas
* **Cadastro e Login:** Validação de unicidade de CNPJ.
* **Dashboard Interativo:** Exibe o total de avaliações recebidas, a **Média Geral de Estrelas** e a lista de avaliações (identificando os usuários pelo E-mail).
* **Herança de Avaliações:** Se uma empresa for cadastrada com um CNPJ que já possui avaliações feitas por usuários no passado, ela as "herda" automaticamente em seu dashboard.
* **Exclusão de Conta:** Deleção completa da conta da empresa.

## 🏗️ Arquitetura MVC (Estrutura do Projeto)

O projeto foi rigorosamente dividido para separar a interface, as regras de negócio e a manipulação de dados:

```text
meu_projeto/
│
├── utils/
│   └── database.py             # Funções genéricas de leitura e escrita de JSON
│
├── models/                     # (M) Manipulação direta dos arquivos .json
│   ├── usuario_model.py
│   ├── empresa_model.py
│   └── avaliacao_model.py
│
├── controllers/                # (C) Regras de negócio, validações e cálculos (Ex: média)
│   ├── usuario_controller.py
│   └── empresa_controller.py
│
├── views/                      # (V) Interface com o usuário (prints e inputs do terminal)
│   ├── main_view.py
│   ├── user_view.py
│   └── empresa_view.py
│
└── main.py                     # Arquivo principal que inicializa o sistema

```

## 🚀 Como Executar

### Pré-requisitos

* **Python 3.x** instalado na sua máquina.

### Instalação e Execução

1. Clone este repositório ou baixe os arquivos do projeto.
2. Abra o terminal e navegue até a pasta raiz do projeto:
```bash
cd caminho/para/o/projeto

```


3. Execute o arquivo principal:
```bash
python main.py

```


*(Dependendo da sua instalação, pode ser necessário usar `python3 main.py`)*

## 💻 Como Utilizar o Sistema

Ao iniciar o programa, você verá a **Tela Inicial**.

1. **Para testar o fluxo completo:** Comece escolhendo a opção `3` e crie um Novo Usuário.
2. Faça o login na opção `1`.
3. No **Painel do Usuário**, escolha avaliar uma empresa (digite um CNPJ fictício, como `111222333`).
4. Saia da conta (Logout) e cadastre uma Nova Empresa na tela inicial (opção `4`) usando o **mesmo CNPJ** que você avaliou.
5. Faça o login como Empresa (opção `2`) e acesse o Dashboard. Você verá que a avaliação feita pelo usuário já estará vinculada a esta empresa.

## 🗄️ Banco de Dados (JSON)

O sistema cria automaticamente uma pasta chamada `database` na raiz do projeto na primeira vez que um dado é salvo.
Dentro dela, os arquivos `usuarios.json`, `empresas.json` e `avaliacoes.json` armazenam as informações em formato de lista de dicionários (`[ {...} ]`).

---

*Desenvolvido como projeto de Fundamentos de Programação para aprofundamento em estruturas de dados, manipulação de arquivos e arquitetura de software.*



