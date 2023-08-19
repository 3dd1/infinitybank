from banco import banco, obterConta

def depositar(conta: int, valor: float) -> None:
    cliente = obterConta(conta)
    if cliente:
        cliente['saldo'] += valor
        print('deposito realizado com sucesso!')
    else:
        print('cliente não encontrado')

