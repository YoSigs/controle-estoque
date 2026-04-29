from rich import print
from rich.table import Table
from rich.panel import Panel

class ControleDeEstoque:
    def __init__(self):
        self.estoque = list()
        self.proximo_id = 1

    def cadastrar_produtos(self):
        #Painel de cadastro de produtos
        painel_cadastro_de_produtos = Panel(f"[blue]Cadastro de Produtos[/]", width=35)
        print(painel_cadastro_de_produtos)

        while True:
            nome = input("Digite o nome do produto: ").strip().title()
            if nome == "":
                print("Digite o nome do produto!")
                continue
            break
        while True:
            try:
                preco = input("Digite o preço do produto R$: ").replace(",", ".")
                preco = float(preco)
                if preco <= 0:
                    print("Digite somente numeros positivos!")
                    continue
                break
            except ValueError:
                print("Digite somente numeros validos!!!")

        while True:
            try:
                quantidade = int(input("Digite a quantidade: "))
                if quantidade <= 0:
                    print("[red]ERRO! numero digitado é menor ou igual a 0[/]")
                    continue
                break
            except ValueError:
                print("[red]Digite somente numeros![/]")
        id = self.proximo_id       
        item = {"id": id,
                "nome": nome,
                "preco": preco,
                "quantidade": quantidade}
        self.proximo_id += 1
        self.estoque.append(item)
        print("Produto cadastrado com sucesso")

    def listar_produtos(self):
        lista = Table(title = "Produtos")

        lista.add_column("ID")
        lista.add_column("Nome")
        lista.add_column("Preço")
        lista.add_column("Quantidade")

        for item in self.estoque:
            lista.add_row(
                str(item["id"]),
                item["nome"],
                f"R$ {item['preco']:.2f}",
                str(item["quantidade"])
            )
            
        print(lista)

    def atualizar_quant_produtos(self):
        self.listar_produtos()
        produto = int(input("Qual o ID do produto que você deseja atualizar? "))
        for i in self.estoque:
            if i["id"] == produto:
                print(f"A quantidade atual do produto {i['nome']} é {i['quantidade']}")
                i["quantidade"] = int(input("Nova quantidade: "))
                print(f"Atualizado: {i['quantidade']} unidades de {i['nome']}")
                
                return
        print("Produto não encontrado")
    
    def deletar_produto(self):
        self.listar_produtos()
        while True:
            try:
                id = input('ID do produto que deseja remover: ').strip()
                
                if id == "":
                    print("[red]ERRO: ID do produto não digitado[/]")
                    continue
                id = int(id)
                for item in self.estoque:
                    if item["id"] == id:
                        confirmacao = input(f"Confirme que deseja excluir o produto {item['nome']}, (S) para confirmar: ").upper()
                        if confirmacao == 'S':
                            self.estoque.remove(item)
                            print("[green]Produto removido com sucesso![/]")
                            return
                        else:
                            print(f"Remoção do produto {item['nome']} cancelada")
                            return
                print("[red]ERRO: Produto não encontrado[/]")
            except ValueError:
                print("[red]ERRO: Digite somente numeros")
            