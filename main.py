from rich import print
import os
from core.estoque import ControleDeEstoque
from core.menu import Menu
from banco.conexao import criar_tabela
                
menu = Menu()
estoque = ControleDeEstoque()

def main():

    criar_tabela()

    while True:
        menu.mostra_menu()
        opcao_menu = str(input("Digite uma opção (0 Para sair): "))
        match opcao_menu:
            case '0':
                print("[red]Fim do programa[/]")
                break
            case '1':
                estoque.cadastrar_produtos()
            case '2':
                estoque.listar_produtos()
            case '3':
                estoque.atualizar_quant_produtos()
            case '4':
                estoque.deletar_produto()
            case _:
                print("[red]OPÇÃO INVALIDA[/]")
        input("\nPressione ENTER para continuar...")
        os.system('cls')

if __name__ == '__main__':
    main()