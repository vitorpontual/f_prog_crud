# Sistema de Gestão - Projeto CRUD em Python

## Sobre o Projeto
Este repositório contém um sistema de gerenciamento via terminal desenvolvido como projeto acadêmico para a disciplina de **[Nome da Disciplina]**. O sistema foi construído com base nos conceitos abordados em sala de aula, focando na implementação de operações **CRUD** (Create, Read, Update, Delete) sem a dependência de bibliotecas externas complexas.

O objetivo principal é construir uma aplicação funcional que demonstre domínio sobre as estruturas de dados nativas do Python e boas práticas de programação, como modularização e tratamento de exceções.

## Conceitos e Estruturas Utilizadas
Para garantir a robustez e organização do código, o projeto faz uso intensivo dos seguintes recursos da linguagem:

* **Listas:** Utilizadas como a "base de dados" principal em memória, armazenando e iterando sobre todos os registros do sistema.
* **Dicionários (Dict):** Responsáveis por modelar as entidades do sistema (ex: `{"id": 1, "nome": "Produto", "quantidade": 5}`), mapeando chaves e valores para facilitar a busca e atualização.
* **Tuplas:** Empregadas para definir dados estáticos e imutáveis durante a execução, como as opções dos menus de navegação ou parâmetros fixos.
* **Funções:** Todo o fluxo do programa é modularizado. Cada operação (adicionar, listar, editar, remover) possui sua própria função, mantendo o arquivo principal limpo e o código reutilizável.
* **Manipulação de Dados:** Tratamento e formatação de strings, conversão de tipos de dados recebidos pelos inputs e formatação da exibição no terminal.
* **Tratamento de Exceções (Try/Except):** Implementado como uma camada de segurança nas interações com o usuário, prevenindo que o programa quebre ao receber valores inesperados (como digitar uma letra quando o sistema espera um número de ID).

## Funcionalidades (CRUD)
- Create (Criar): Adição de novos registros validados no sistema.
- Read (Ler): Exibição de todos os registros armazenados ou busca detalhada por identificador.
- Update (Atualizar): Modificação de atributos específicos de um registro existente.
- Delete (Excluir): Remoção segura de registros, com confirmação e validação de existência.

## Como Executar
1. Certifique-se de ter o [Python 3.x](https://www.python.org/downloads/) instalado na sua máquina.
2. Clone este repositório ou baixe os arquivos fonte.
3. Navegue até o diretório do projeto no seu terminal.
4. Execute o arquivo principal:
   ```bash
   python main.py
   ```

## Autor
Squad 10.1 - Desenvolvimento inicial
