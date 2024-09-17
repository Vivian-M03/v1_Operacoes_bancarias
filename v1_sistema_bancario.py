print('\n=============SEJA BEM VINDO AO BANCO ORION!=============')
menu = """
    Escolha uma opção
    [1] Extrato
    [2] Deposito
    [3] Saque
    [4] Sair
"""

saldo = 1500.0
valor_limite_saque = 500.0
LIMITE_SAQUE = 3
historico_depositos = []
historico_saque = []
salto_anterior = [saldo]

while True:
    print(menu)
    opcao = input('Operação desejada: ')

    if opcao == '1':
        print('\n============ EXTRATO =============')
        print(f'\nSalto: R$ {saldo: .2f}')
        print('\nVolte sempre!')

    elif opcao == '2':
        valor_deposito = float(input('Digite o valor que deseja depositar: R$ '))
        saldo += valor_deposito
        historico_depositos.append(valor_deposito)
        print(f'\nDepósito de R$ {valor_deposito:.2f} realizado com sucesso!')
        print('\nRetornando ao menu...')
    
    elif opcao == '3':
        valor_saque = float(input('Informe o valor que deseja sacar: R$ '))
        print()
        if LIMITE_SAQUE > 0:
            if valor_saque <= valor_limite_saque:
                if valor_saque <= saldo:
                    valor_limite_saque -= 1
                    saldo -= valor_saque
                    print(' ---------------- SUCESSO! ---------------- ')
                    print(f'      Saque de R$ {valor_saque: .2f} realizado.')

                    historico_saque.append(valor_saque)
                else:
                    print(' ------- ERRO! ------- ')
                    print('\nVALOR INDISPONÍVEL PARA SAQUE!') 
            else:
                print(' ------- ERRO! ------- ')
                print('\nVALOR EXEDE LIMITE PARA SAQUE!')
        else:
            print(' ------- ERRO! ------- ')
            print('\nLIMITE DE SAQUE ATINGIDO!')
        
        print('\nOperaçõa finalizada...')
    
    elif opcao == '4':
        print('\nO BANCO ORION AGRADECE A PREFERÊNCIA')
        print()
        break
    else:
        print('\n Operação Inválida. Tente novamente!')
        print()


            
             


    









   

