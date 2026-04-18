from rich import print
from rich.table import Table
from rich.panel import Panel

class Menu:

    def mostra_menu(self):
        conteudo = f"[blue]1.[/] Cadastrar produtos"
        conteudo += f"\n[blue]2.[/] Listar produtos"
        conteudo += f"\n[blue]3.[/] Atualizar quantidade"
        conteudo += f"\n[blue]4.[/] Deletar produto"

        menu = Panel(conteudo, width=35, title="Menu")
        print(menu)