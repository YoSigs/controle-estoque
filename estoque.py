from rich import print
from rich.table import Table
from rich.panel import Panel
import validacoes
from banco.produtos import inserir_no_banco, lista_de_produtos

class ControleDeEstoque:
    def __init__(self):
        self.estoque = list()
        self.proximo_id = 1

    def cadastrar_produtos(self):
        painel_cadastro_de_produtos = Panel(f"[blue]Cadastro de Produtos[/]", width=35)
        print(painel_cadastro_de_produtos)

        while True:
            nome = input("Digite o nome do produto (0 para voltar): ").strip().title()
            if nome == "":
                print("Digite o nome do produto!")
                continue
            elif nome == '0':
                return
            break
        while True:
            try:
                preco = input("Preço do produto: ").replace(",", ".")
                preco = float(preco)
                if not validacoes.verifica_numero_positivo(preco):
                    print("[red]Digite somente numeros positivos![/]")
                    continue
                break
            except ValueError:
                print("Digite somente numeros!!!")

        while True:
            quantidade = validacoes.ler_inteiros("Digite a quantidade: ")
            if not validacoes.verifica_numero_positivo(quantidade):
                print("[red]Digite somente numeros positivos![/]")
                continue
            break
        inserir_no_banco(nome=nome, preco=preco, quantidade=quantidade)
                
        id = self.proximo_id       
        item = {"id": id,
                "nome": nome,
                "preco": preco,
                "quantidade": quantidade}
        self.proximo_id += 1
        self.estoque.append(item)
        print("[green]Produto cadastrado com sucesso[/]")

    def mostrar_produtos(self):
        if validacoes.verifica_estoque(self.estoque) == False:
            return
        else:
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

    def listar_produtos(self):
        lista = Table(title = "Produtos")

        lista.add_column("ID")
        lista.add_column("Nome")
        lista.add_column("Preço")
        lista.add_column("Quantidade")

        for produto in lista_de_produtos():
            lista.add_row(
                str(produto[0]),
                produto[1],
                f"R$ {produto[2]:.2f}",
                str(produto[3])
            )
            
        print(lista)

    def atualizar_quant_produtos(self):
        #verifica se o estoque ja existe
        if validacoes.verifica_estoque(self.estoque) == False:
            return
        
        #mostra todos os possiveis produtos
        self.mostrar_produtos()

        while True:
            #recebe o id do produto a ser atualizado
            produto = int(input("Qual o ID do produto que você deseja atualizar? (0 para voltar)"))

            #verifica se o numero é positivo
            if not validacoes.verifica_numero_positivo(produto):
                print("[red]Digite somente numeros positivos![/]")  
                continue
            break

        #verifica se o numero é igual a 0
        if produto == 0:
            return
        
        
        for i in self.estoque:
            if i["id"] == produto:
                print(f"A quantidade atual do produto {i['nome']} é {i['quantidade']}")
                i["quantidade"] = int(input("Nova quantidade: "))
                print(f"Atualizado: {i['quantidade']} unidades de {i['nome']}")
                return
        print("[red]ERRO: produto não encontrado!")
    
    def deletar_produto(self):
        if validacoes.verifica_estoque(self.estoque) == False:
            return
        else:
            self.mostrar_produtos()
            while True:
                try:
                    id = validacoes.ler_inteiros("ID do produto que deseja remover: (0 para voltar) ")
                    if id == '0':
                        return
                    
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
                                print(f"Remoção do produto {item['nome']} [red]cancelada[/]")
                                return
                    print("[red]ERRO: Produto não encontrado[/]")
                except ValueError:
                    print("[red]ERRO: Digite somente numeros[/]")
                