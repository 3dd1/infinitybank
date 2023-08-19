from banco import *
from operacoes.deposito import depositar
from operacoes.consulta import consultarSaldo
from operacoes.saque import sacar
from operacoes.transferencia import transferir

def menu():
    while True:
        print('---- sistema bancário ----')
        print('1 - adicionar conta')
        print('2 - editar conta')
        print('3 - consultar conta')
        print('4 - apagar conta')
        print('5 - listar contas')
        print('6 - atualizar nome')
        print('7 - atualizar saldo')
        print('8 - realizar saque')
        print('9 - realizar deposito')
        print('10 - consultar saldo')
        print('11 - transferencia')
        print('12 - sair')
        opcao = input('digite a opção: ')