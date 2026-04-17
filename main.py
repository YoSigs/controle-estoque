from rich import print
from rich.table import Table
from rich.panel import Panel
import os

class Menu:
    def __init__(self):
        self.estoque = list()

    def mostra_menu(self):
        os.system('cls')
        conteudo = f"[blue]1.[/] Cadastrar produtos\n"
        conteudo += f"[blue]2.[/] Listar produtos\n"
        conteudo += f"[blue]3.[/] Atualizar quantidade"

        menu = Panel(conteudo, width=35, title="Menu")
        print(menu)

    def cadastrar_produtos(self):
        os.system('cls')
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
        os.system('cls')
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
        
                
c1 = Menu()

while True:
    c1.mostra_menu()
    opcao_menu = str(input("Digite uma opção: "))
    match opcao_menu:
        case '0':
            print("Fim do programa")
            break
        case '1':
            c1.cadastrar_produtos()
        case '2':
            c1.listar_produtos()
        case '3':
            c1.atualizar_quant_produtos()
        case _:
            print("OPÇÃO INVALIDA")
    input("\nPressione ENTER para continuar...")