# Sistema de Controle de Estoque (CLI)

Projeto desenvolvido em Python para gerenciamento de estoque via terminal, utilizando SQLite para persistência de dados e Rich para exibição das informações no console.

## Funcionalidades

* Cadastro de produtos
* Listagem de produtos
* Busca de produtos por ID
* Atualização de quantidade
* Exclusão de produtos
* Validação de entradas do usuário

## Tecnologias

* Python
* SQLite
* Rich

## Estrutura do Projeto

```text
controle-estoque/
│
├── banco/
│   ├── conexao.py
│   └── produtos.py
│
├── validacoes.py
├── estoque.py
├── main.py
└── README.md
```

## Como Executar

1. Clone o repositório:

```bash
git clone <url-do-repositorio>
```

2. Acesse a pasta do projeto:

```bash
cd controle-estoque
```

3. Instale as dependências:

```bash
pip install rich
```

4. Execute o sistema:

```bash
python main.py
```

## Aprendizados

Durante o desenvolvimento deste projeto foram praticados conceitos como:

* CRUD com SQLite
* Modularização de código
* Validação de dados de entrada
* Manipulação de banco de dados com Python
* Uso da biblioteca Rich para interface em terminal

