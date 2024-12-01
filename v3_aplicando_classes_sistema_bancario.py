from abc import ABC, ABCMeta, abstractclassmethod, abstractproperty
from datetime import datetime
import textwrap

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

#chama o construtor da classe pai(Cliente)
class PessoaFisica(Cliente):
    def __init__(self, endereco, nome, cpf, data_nascimento ): ##atribuições
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento   

class Conta:
    def __init__(self, cliente, numero):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, numero, cliente):
        return cls(cliente, numero)

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property 
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print(' ------- ERRO! ------- ')
            print('\nValor Exede Limite!')
        
        elif valor > 0:
            self._saldo -= valor
            print(' ------- SUCESSO! ------- ')
            print('\n--- Saque Realizado com Sucesso! --- ')
            return True
        
        else:
            print(' ------- ERRO! ------- ')
            print('\nValor Indisponível Para Saque!')
        
        return False
    
    def deposito(self, valor):
        if valor > 0:
           self._saldo += valor
           print('\n==== Deposito realizado com sucesso! ====')
           return True
        else:
            print('\n\n Operaçõa falhou! Valor informato é invalido.\n')
            return False

class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite = 1000, limite_saque = 3):
        super().__init__(cliente, numero)
        self.limite = limite
        self.limite_saque = limite_saque
    
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__])
        
        excedeu_limite = valor > self.limite
        exedeu_saque = numero_saques >= self.limite_saque

        if excedeu_limite:
            print(' ------- ERRO! ------- ')
            print('\n--- O valor do saque excede o limite. Tente Novamente! ---')
        
        elif exedeu_saque:
            print(' ------- ERRO! ------- ')
            print('\n--- Número máximo de saques excedido. Tente Novamente! ---')
        
        else:
            return super().sacar(valor)

    def __str__(self):
        return f"""\
                Agência:\t{self.agencia}
                Númedo da Conta Corrente:\t{self.numero}
                Títular:\t{self.cliente.nome}
        """

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.deposito(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Historico:
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"), #Adicionado
            }
        )

def menu():
    menu = """\n
    ============= SEJA BEM VINDO AO BANCO ORION! =============
    Escolha uma opção
    [1] Deposito
    [2] Saque
    [3] Extrado
    [4] Nova conta
    [5] Listar contas
    [6] Novo usuário
    [7] Sair
    ==> """
    return input(textwrap.dedent(menu))

#debugar
def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print('\n=== ERRO! ===')
        print('\n Cliente não possui conta! ')
        return
    #pedir numero da conta
    return cliente.contas[0]

def depositar(clientes):
    cpf = input('Insira o número de CPF: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('\n=== ERRO! ===')
        print('\nCliente não encontrado!')
        return
    
    valor = float(input('Digite o valor do depósito: R$ '))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input('Insira o número de CPF: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('\n=== ERRO! ===')
        print('\nCliente não encontrado!')
        return
    
    valor = float(input('Digite o valor do saque: R$ '))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input('Insira o número de CPF: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('\n=== ERRO! ===')
        print('\nCliente não encontrado!')
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print('\n ==== EXTRATO ====')
    transacoes = conta.historico.transacoes

    extrato = ''
    if not transacoes:
        extrato = 'Não foi possivel localizar nenhuma movimentação.'
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR${transacao['valor']:.2f}"
    
    print(extrato)
    print(f'\nSaldo:\n\tR$ {conta.saldo:.2f}')
    print('----------------------------------------')

def criar_cliente(clientes):
    cpf = input('Insira o número de CPF: ')
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print('\n==== ERRO! ====')
        print('\nCPF já cadastrado!')
        return
    
    nome = input('\nNome completo: ')
    data_nascimento = input('\nInforme sua data de nacimento (dd-mm-aaaa): ')
    endereco = input('\nInforme seu endereço (lagradouro, bairro - nro - cidade/sigla estado): ')

    cliente = PessoaFisica(endereco=endereco, nome=nome, cpf=cpf, data_nascimento=data_nascimento)
    
    clientes.append(cliente)

    print('\n==== Cliente Cadastrato com Sucesso! ====')

def criar_conta(numero_conta, clientes, contas):
    cpf = input('Insira o número de CPF: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
       print('\n=== ERRO! ===')
       print('\nCliente não encontrado, criação de conta encerrada!')
       return
    #consultor
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print('\n==== Conta Criada com Sucesso! ====')

def listar_contas(contas):
    for conta in contas:
        print('=' * 100)
        print(textwrap.dedent(str(conta))) #representação
  
def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == '1':
            depositar(clientes)
        
        elif opcao == '2':
            sacar(clientes)
        
        elif opcao == '3':
            exibir_extrato(clientes)
        
        elif opcao == '4':
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        
        elif opcao == '5':
            listar_contas(contas)
        
        elif opcao == '6':
            criar_cliente(clientes)
        
        elif opcao == '7':
            break

main()
 