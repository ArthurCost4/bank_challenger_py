from abc import ABC, abstractmethod

class Transacao(abc):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    @property
    def valor(self):
        return self.__valor

    @abstractmethod
    def registrar(conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

class Cliente:
    def __init__(self, **kwargs):
        self.__endereco = kwargs.get('endereco', 'n especificado')
        self.__contas = kwargs.get('ccntas', 'n especificado')
    
    def realizar_transacao(conta, transacao):
        transacao.registrar(conta)
    
    def adcionar_conta(conta):
        return conta

class Historico:
    def __init__(self):
        self.__transacoes = []

    @property
    def transacoes(self):
        return self.__transacoes

    def adcionar_transacao(transacao):
        return transacao

class Conta:
    def __init__(self, **kwargs):
        self.__saldo = kwargs.get('saldo', 'n especificado')
        self.__numero = kwargs.get('numero', 'n especificado')
        self.__agencia = kwargs.get('agencia', 'n especificado')
        self.__cliente = kwargs.get('Cliente', 'n especificado')
        self.__historico = kwargs.get('Historico', 'n especificado')

    def saldo_disponivel(self):
        print(f"{self.__saldo}")

    @classmethod
    def nova_conta(cliente,):
        return cliente
    
    def sacar(valor):
        return valor
    
    def depositar(valor):
        return True
    

class PessoaFisica(Cliente):
    def __init__(self, **kwargs):
        self.__cpf = kwargs.get('cpf', 'n especificado')
        self.__nome = kwargs.get('nome', 'n especificado')
        self.__data_nascimento = kwargs.get('data_nascimento', 'n especificado')
        super().__init__(**kwargs)
    
class ContaCorrente(Conta):
    def __init__(self, **kwargs):
        self.__limite = kwargs.get('limite', 'n especificado')
        self.__limite_saques = kwargs.get('limite_saques', 'sexo')
        super().__init__(**kwargs)

