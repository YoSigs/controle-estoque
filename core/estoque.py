from rich import print
from rich.table import Table
from rich.panel import Panel
import utils.validacoes as validacoes
from banco.produtos import *

class ControleDeEstoque:

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

        print("[green]Produto cadastrado com sucesso[/]")

    def mostrar_produtos(self):
        
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

    def listar_produtos(self):
        lista = Table(title = "Produtos")

        lista.add_column("ID")
        lista.add_column("Nome")
        lista.add_column("Preço")
        lista.add_column("Quantidade")

        filtro = input("Digite o nome do produto para filtrar apenas ele, ou aperte enter para ver todos: ")
        if filtro.strip() == "":
            for produto in lista_de_produtos():
                lista.add_row(
                str(produto[0]),
                produto[1],
                f"R$ {produto[2]:.2f}",
                str(produto[3])
            )
        else:
           produto = filtrar_produtos_por_nome(filtro)
           if not produto:
               print("[red]ERRO: Produto não encontrado![/]")
               return
           
           for produto in filtrar_produtos_por_nome(filtro):
                lista.add_row(str(produto[0]),
                            produto[1],
                            f"R$ {produto[2]:.2f}",
                            str(produto[3]))
            
                
            
        print(lista)

    def atualizar_quant_produtos(self):

        self.mostrar_produtos()
        while True:
            id_produto = validacoes.ler_inteiros("Qual o ID do produto que você deseja atualizar? (0 para voltar)")
            if id_produto == 0:
                return
        
            if not validacoes.verifica_numero_positivo(id_produto):
                print("[red]Digite somente numeros positivos![/]")  
                continue
            break

        produto = filtrar_produtos_por_id(id_produto)
        if not produto:
            print("[red]ERRO: Produto não encontrado![/]")
            return
        
        while True:
            quantidade_nova = validacoes.ler_inteiros(f"A quantidade atual do produto {produto[1]} é {produto[3]} \nNova quantidade: ")

            if not validacoes.verifica_numero_positivo(quantidade_nova):
                print("[red]ERRO: digite somente numeros positivos")
                continue
            
            atualizar_quantidade(id_produto, quantidade_nova)
            print("[green]Quantidade atualizada com sucesso!!![/]")
            break

    
    def deletar_produto(self):
        produtos = lista_de_produtos()
        if not produtos:
            print("[red]ERRO: não há produtos cadastrados[/]")
            return
        
        id_produto = validacoes.ler_inteiros("ID do produto que deseja remover: (0 para voltar) ")
        if id_produto == 0:
            return
        produto = filtrar_produtos_por_id(id_produto)
        if produto is None:
            print(F"[red]ERRO: Produto não encontrado![/]")
            return
        
        confirmacao = input(f"Confirme que deseja excluir o produto {produto[1]}, (S) para confirmar: ").upper()
        if confirmacao == 'S':
            apagar_produto(id_produto)
            print(f"[green]Produto {produto[1]} removido com sucesso![/]")
            return
        
        print(f"Remoção do produto {produto[1]} [red]cancelada[/]")
        return
                
                