from rich import print
from rich.console import Console
console = Console()

def verifica_estoque(estoque):
    if not estoque:
        print('[red]ERRO: o estoque está vazio[/]')
        return False
    return True

def verifica_numero_positivo(numero):
    try:
        numero = float(numero)
        if numero < 0:
            return False
        return True
    except ValueError:
        return
        
def ler_inteiros(msg):
    while True:
        valor = console.input(msg)
        valor = valor.strip()
        if valor == "":
            print("[red]ERRO: Campo vazio!")
            continue
        elif valor.isnumeric():
            valor = int(valor)
            return valor
        else:
            print("[red]ERRO: Digite somente números!")

def ler_float(msg):
    while True:
        valor = console.input(msg)
        valor = valor.strip()
        if valor == "":
            print("[red]ERRO: Campo vazio!")
            continue
        try:
            valor = float(valor)
            return valor
        except ValueError:
            print("[red]ERRO: Digite somente números!")
