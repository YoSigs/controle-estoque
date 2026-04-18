from rich import print
from rich.table import Table
from rich.panel import Panel

class ControleDeEstoque:
    def __init__(self):
        self.estoque = list()

    def cadastrar_produtos(self):
        #Painel de cadastro de produtos
        painel_cadastro_de_produtos = Panel(f"[blue]Cadastro de Produtos[/]", width=35)
        print(painel_cadastro_de_produtos)

        
        nome = str(input("Digite o nome do produto: "))
        preco = float(input("Digite o preço do produto R$: "))
        quantidade = int(input("Digite a quantidade: "))
        item = {"nome": nome, "preco": preco, "quantidade": quantidade}
        self.estoque.append(item)
        print("Produto cadastrado com sucesso")

    def listar_produtos(self):
        lista = Table(title = "Produtos")

        lista.add_column("Nome")
        lista.add_column("Preço")
        lista.add_column("Quantidade")

        for item in self.estoque:
            lista.add_row(
                item["nome"],
                f"R$ {item['preco']:.2f}",
                str(item["quantidade"])
            )
            
        print(lista)

    def atualizar_quant_produtos(self):
        self.listar_produtos()
        produto = str(input("Qual produto você deseja atualizar? "))
        for i in self.estoque:
            if i["nome"] == produto:
                print(f'A quantidade atual do produto {produto} é {i["quantidade"]}')
                i["quantidade"] = int(input("Nova quantidade: "))
                print(f"Atualizado: {i['quantidade']} unidades de {i['nome']}")
                
                return
        print("Produto não encontrado")
    
    def deletar_produto(self):
        self.listar_produtos()
        nome = str(input('Nome do produto que deseja remover: '))

        for item in self.estoque:
            if item["nome"] == nome:
                self.estoque.remove(item)
                print("[green]Produto removido com sucesso![/]")
                return
        print("[red]ERRO: Produto não encontrado[/]")