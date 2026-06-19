from rich import print

def verifica_estoque(estoque):
    if not estoque:
        print('[red]ERRO: o estoque está vazio[/]')
        return False
    return True

def verifica_numero_positivo(numero):
    if numero < 0:
        return False
    return True
        
def ler_inteiros(msg):
    while True:
        valor = input(msg)
        valor = valor.strip()
        if valor == "":
            print("[red]ERRO: Campo vazio!")
            continue
        elif valor.isnumeric():
            valor = int(valor)
            return valor
        else:
            print("[red]ERRO: Digite somente números!")
