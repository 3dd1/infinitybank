from typing import Optional
from time import sleep
banco = [
    {"conta": 1, "cliente": "Luis", "saldo": 1000.0},
    {"conta": 2, "cliente": "Mariana", "saldo": 2500.0}
]

conta_atual = 2

def adicionarConta(cliente: str, saldo: float) -> None:
    global conta_atual
    conta_atual += 1
    conta = {
        "conta": conta_atual,
        "cliente": cliente,
        "saldo": saldo
    }
    banco.append(conta)
    print('Conta cadastra com sucesso!')

def obterConta(conta: int) ->Optional[dict or None]:
    for cliente in banco:
        if cliente["conta"] == conta:
            return cliente
    return None


def deletarConta(conta: int) -> None:
    cliente = obterConta(conta)
    if cliente:
        banco.remove(cliente)
        print("cliente removido com sucesso!")
    else:
        print("cliente não encontrado!")


def listarContas() -> None:
    for cliente in banco:
        print("--- Dados do cliente ----")
        print(f"N. Conta: {cliente['conta']}")
        print(f"Cliente: {cliente['cliente']}")
        print(f"Saldo: {cliente['saldo']}")
        print("----------------------------------")
        sleep(2)

def atualizarNome(conta: int, novo_nome: str) -> None:
    cliente = obterConta(conta)
    if cliente:
        cliente['cliente'] = novo_nome
        print('dados alterados com sucesso!')
    else:
        print('Cliente não encontrado!')

def atualizarSaldo(conta: int, novo_saldo: str) -> None:
    cliente = obterConta(conta)
    if cliente:
        cliente['saldo'] = novo_saldo
        print('dados alterados com sucesso!')
    else:
        print('Cliente não encontrado!')