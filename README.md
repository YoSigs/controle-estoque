# Sistema de Controle de Estoque (CLI)

Projeto desenvolvido em Python para gerenciamento de estoque via terminal, utilizando SQLite para persistência de dados e Rich para exibição das informações no console.

## Funcionalidades

- Cadastro de produtos
- Listagem de produtos
- Busca de produtos por nome
- Atualização de quantidade
- Atualização de preço
- Exclusão de produtos
- Validação de entradas do usuário

## Tecnologias

- Python
- SQLite
- Rich

## Estrutura do Projeto

```text
controle-estoque/
│
├── banco/
│   ├── conexao.py
│   └── produtos.py
│
├── core/
│   ├── estoque.py
│   └── menu.py
│
├── utils/
│   └── validacoes.py
│
├── tests/
│   └── teste.py
│
├── main.py
├── README.md
└── .gitignore
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

- CRUD com SQLite
- Consultas SQL utilizando SELECT, INSERT, UPDATE e DELETE
- Modularização de código
- Validação de dados de entrada
- Manipulação de banco de dados com Python
- Uso da biblioteca Rich para interface em terminal
- Organização de projetos Python em múltiplos módulos

## Próximos Passos

- Implementar logs da aplicação
- Adicionar testes automatizados
- Melhorar a experiência do usuário no terminal
- Implementar validação utilizando Pydantic