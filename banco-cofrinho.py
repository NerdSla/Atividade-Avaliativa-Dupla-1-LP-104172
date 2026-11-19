import os

saldo = 500.00
extrato = []

def menu():
    os.system('cls')
    print('=== BANCO COFRINHO | CAIXA ===')
    print('1 - Ver saldo')
    print('2 - Depositar')
    print('3 - Sacar')
    print('4 - Ver extrato')
    print('0 - Sair')

def ver_saldo(saldo):
    print('--- SALDO ---')
    print(f'Saldo: R$ {saldo:.2f}')
    input('Pressione ENTER para voltar ao menu...')

def dep_saldo(saldo, extrato):
    print('--- DEPÓSITO ---')
    valor = float(input('Digite quanto você quer depositar: '))
    if valor <= 0:
        print('Valor inválido\n')
        input('Pressione ENTER para voltar ao menu...')
        return saldo
    extrato.append(f'Depósito: R$ {valor:.2f}')
    saldo += valor
    input('Depósito realizado com sucesso\nPressione ENTER para voltar ao menu...')
    return saldo

def sac_saldo(saldo, extrato):
    print('--- SAQUE ---')
    valor = float(input('Digite quanto você deseja sacar: '))
    if valor <= 0:
        print('Recusado!')
        print('Valor a ser sacado tem que ser maior que 0')
        input('Pressione ENTER para voltar ao menu...')
        return saldo
    elif valor > saldo:
        print('Recusado!')
        print('Valor a ser sacado não pode ser maior que o saldo atual.')
        input('Pressione ENTER para voltar ao menu...')
        return saldo
    print('Aprovado')
    extrato.append(f'Saque: R$ {valor:.2f}')
    saldo -= valor
    input('Saque realizado com sucesso\nPressione ENTER para voltar ao menu...')
    return saldo

def mostrar_extrato(saldo, extrato):
    if len(extrato) == 0:
        print('Nenhuma movimentação')
    else:
        for i, extratos in enumerate(extrato):
            print(f'{i+1}º Extrato: {extratos}')
        print(f'Saldo: R$ {saldo}')
    input('Pressione ENTER para voltar ao menu...')

while True:
    menu()
    opcao = input('Digite o número correspondente ao menu ( 1 | 2 | 3 | 4 | 0 ): ')
    match opcao:
        case '1':
            ver_saldo(saldo)
        case '2':
            saldo = dep_saldo(saldo, extrato)
        case '3':
            saldo = sac_saldo(saldo, extrato)
        case '4':
            mostrar_extrato(saldo, extrato)
        case '0':
            print('Fechando o programa...')
            exit()
        case _:
            print('Opção inválida')
            input('Digite ENTER para voltar ao menu...')