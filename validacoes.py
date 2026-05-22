from rich import print

def verifica_estoque(estoque):
    if not estoque:
        print('[red]ERRO: o estoque está vazio[/]')
        return False
    return True

        
    