from random import randint

class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print(f'Caixa abaixo do nível recomendado.\nCaixa atual: R${self.caixa}')
        else:
            print(f'O valor do caixa está ok.\nCaixa atual: R${self.caixa}')

    def emprestar_dinheiro(self, montante, cpf, juros):
        if self.caixa > montante:
            self.emprestimos.append((montante, cpf, juros))
        else:
            print('Valor em caixa insuficiente para empréstimo.')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


class AgenciaVirtual(Agencia):

    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 1000000
        self.caixa_paypal = 0

    def depositar_paypal(self, montante):
        self.caixa -= montante
        self.caixa_paypal += montante

    def sacar_paypal(self, montante):
        self.caixa_paypal -= montante
        self.caixa += montante


class AgenciaComum(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 1000000

class AgenciaPremium(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 10000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print('Cliente sem patrimônio mínimo necessáiro para agência premium.')

