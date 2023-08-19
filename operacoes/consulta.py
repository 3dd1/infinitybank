from banco import obterConta, banco

def consultarSaldo(conta: int) -> None:
    cliente = obterConta(conta)
    if cliente:
        print(f"Seu saldo: {cliente['saldo']}")
    else:
        print('cliente não encontrado!')
