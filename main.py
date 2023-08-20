import banco
from switchcase.switchcase import switch
from banco import *
from operacoes.deposito import depositar
from operacoes.consulta import consultarSaldo
from operacoes.saque import sacar
from operacoes.transferencia import transferir
def continuar():
    if(int(input("Deseja continuar? \n1- SIM 2- NAO\n")) == 1):
        menu()
    else:
        print("Obrigado!")
def menu():
    while True:
        print('---- sistema bancário ----')
        print('1 - adicionar conta')
        print('2 - editar conta')
        print('3 - consultar conta')
        print('4 - apagar conta')
        print('5 - listar contas')
        print('6 - atualizar nome') #redundancia do carai
        print('7 - atualizar saldo')
        print('8 - realizar saque')
        print('9 - realizar deposito')
        print('10 - consultar saldo')
        print('11 - transferencia')
        print('12 - sair')
        opcao = int(input('digite a opção: '))
        for case in switch(opcao):
            if case(1):
                print('---- Adicionar Conta ----')
                nome = input("Digite seu nome: ")
                saldo = float(input("Digite o saldo da conta: "))
                adicionarConta(nome,saldo)
                continuar()
                break
            if case(2):
                print('---- Editar Conta ----')
                atualizarNome(int(input("Digite o número da conta: ")), input("Digite o novo nome do cliente: "))
                continuar()
                break
            if case(3):
                print('---- Consultar Conta ----')
                consultarConta(int(input("Digite o número da conta que deseja consultar: ")))
                continuar()
                break
            if case(4):
                print('---- Apagar Conta ----')
                conta = int(input("Digite o número da conta que deseja apagar: "))
                print("DADOS DA CONTA:\n")
                consultarConta(conta)
                pergunta = int(input("\n!!! TEM CERTEZA QUE DESEJA APAGAR ESTA CONTA ? !!! \n1 - SIM 2 - NAO\n"))
                if pergunta == 1:
                    deletarConta(conta)

                continuar()
                break
            if case(5):
                print('---- Listar Contas ----')
                listarContas()
                continuar()
                break
        break



menu()
