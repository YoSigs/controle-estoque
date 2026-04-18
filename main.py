from rich import print
from rich.table import Table
from rich.panel import Panel
import os
from estoque import ControleDeEstoque
from menu import Menu
                
menu = Menu()
estoque = ControleDeEstoque()

while True:
    menu.mostra_menu()
    opcao_menu = str(input("Digite uma opção: "))
    match opcao_menu:
        case '0':
            print("Fim do programa")
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
            print("OPÇÃO INVALIDA")
    input("\nPressione ENTER para continuar...")
    os.system('cls')