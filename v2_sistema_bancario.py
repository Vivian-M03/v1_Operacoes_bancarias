import textwrap

def menu():
    print('\n=============SEJA BEM VINDO AO BANCO ORION!=============')
    menu = """\n
    Escolha uma opção
    [1] Extrato
    [2] Deposito
    [3] Saque
    [4] Nova conta
    [5] Listar contas
    [6] Novo usuário
    [7] Sair
    ==> """
    return input(textwrap.dedent(menu))
  

def exibir_extrato(saldo, /, *, extrato):
    if extrato == '':
        print('\n============ EXTRATO =============')
        if extrato == '':
            print('Não foram realizadas transações.')
        else:
            print(f"\nSalto:\t\tR$ {saldo:.2f}")
        print('==================================')

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Deposito:\tR$ {valor:.2f}\n'
        print('\n==== Deposito realizado com sucesso! ====')
    else:
        print('\n\n Operaçõa falhou! Valor informato é invalido.\n')
    
    return saldo, extrato

def saque(*, saldo, valor, limite, extrato,numero_saques, limite_saques):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques >= limite_saques

    if excedeu_saldo:
        print(' ------- ERRO! ------- ')
        print('\nVALOR EXEDE LIMITE PARA SAQUE!')
    
    elif excedeu_limite:
        print(' ------- ERRO! ------- ')
        print('\nVALOR INDISPONÍVEL PARA SAQUE!')
    
    elif excedeu_saque:
        print(' ------- ERRO! ------- ')
        print('\nLIMITE DE SAQUE ATINGIDO!')
    
    elif valor > 0:
        print('\n ---------------- SUCESSO! ---------------- \n')
        saldo -= valor
        extrato += (f'Saque:\t\tR$ {saldo:.2f} realizado')
        numero_saques += 1
        print(extrato)
    else:
        print('\nOperação falho! Valir informato é invalido')
        print('\nOperaçõa finalizada...')
    
    return saldo, extrato

def criar_usuario(usuarios):
    print('\n ------- Insira seus dados e torne-se um Orionzinho -------')
    cpf = input('\nInsira seu CPF (apenas caracteres númericos): ')
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print('\n--------- ERRO! ---------')
        print('\nUsuario já cadastrato!')
        return
    
    nome = input('\nNome completo: ')
    data_nascimento = input('\nInforme sua data de nacimento (dd-mm-aaaa): ')
    endereco = input('\nInforme seu endereço (lagradouro, bairro - nro - cidade/sigla estado): ')
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "endereço": endereco})
    print(usuario)
    print('\n------- BEM VINDO(a) AO UNIVERSO ORION! -------')
    print('\n Usuario cadastrato com sucesso!')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf ]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('\nInsira o CPF do usuario: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n------- Conta criada com sucesso! -------')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    
    print('\n Usuário não encontrado, inicie o processo de criação de conta!')

def listar_contas(contas):
    for conta in contas:
        cadastro = f"""\
                Agência: \t{conta['agencia']}
                Númedo da Conta:\t\t{conta['numero_conta']}
                Títular:\t\t{conta['usuario']['nome']}
        """
        print('=' * 100)
        print(textwrap.dedent(cadastro))

def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    nova_conta = []

    while True:
        opcao = menu()
        #chamando a função exibir_extrato
        if opcao == '1':
            exibir_extrato(saldo, extrato=extrato)
        #chamando a função deposito
        elif opcao == '2':

            valor = float(input('\nDigite o valor do deposito: '))
            saldo, extrato = deposito(saldo, valor, extrato)
        #chamando a função saque
        elif opcao == '3':

            valor = float(input('\nDigite o valor do saque: '))
            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUE,
                ) 
        #chama a função criar_usuario
        elif opcao == '4':
            criar_usuario(usuarios)
        #chamando a função criar_conta
        elif opcao == '5':
             listar_contas(contas)
       
        #chamando a função listar_conta
        elif opcao == '6':
            numero_conta = len(contas) + 1
            nova_conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if nova_conta:
                contas.append(contas)
        
        elif opcao == '7':
            print('\nO BANCO ORION AGRADECE A PREFERÊNCIA')
            print()
            break
        else:
            print('\n Operação Inválida. Tente novamente!')
            print()
main()