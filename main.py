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
        print('6 - realizar saque')
        print('7 - realizar deposito')
        print('8 - consultar saldo')
        print('9 - transferencia')
        print('10 - sair')
        opcao = int(input('digite a opção: '))
        if opcao not in range(1,10):
            print("!!! DIGITE UM NUMERO DE 1 A 10 !!!")
            sleep(2)
            menu()
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
            if case(6):
                print('---- Sacar dinheiro ----')
                sacar(int(input("Digite o numero da conta: ")), float(input("Digite o valor do saque: R$ ")))
                continuar()
                break
            if case(7):
                print('---- Depositar dinheiro ----')
                depositar(int(input("Digite o numero da conta que deseja realizar o deposito: ")), float(input("Digite o valor do deposito: R$ ")))
                continuar()
                break
            if case(8):
                print('---- Consultar saldo ----')
                consultarSaldo(int(input("Digite o numero da conta: ")))
                continuar()
                break
            if case(9):
                print('---- Transferir dinheiro ----')
                contaOrig = int(input("Digite o número da conta origem: "))
                consultarConta(contaOrig)
                contaDest = int(input("Digite o numero da conta destino: "))
                consultarConta(contaDest)
                transferir(contaOrig,contaDest,float(input("Digite o valor da transferencia: R$ " )))
                continuar()
                break
            if case(10):
                print("Obrigado !")
                break
        break



menu()
