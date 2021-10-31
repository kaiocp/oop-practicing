from datetime import datetime
import pytz
from random import randint

class ContaCorrente:
    """
    Cria um objeto conta corrente para gerenciar as contas dos clientes

    Atributos:
        nome (str): Nome do Cliente
        cpf (str): CPF do Cliente
        saldo (float): Saldo disponível na conta corrente
        agencia (int): Agência responsável pela conta do cliente
        num_conta (int): Número da Conta Corrente do cliente
        limite (float): Limite de cheque especial do cliente
        transações (list): Lista com histórico de transações do cliente

        Para mais informações sobre docstring consultar PEP-257
    """

    @staticmethod
    def _data_e_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self._saldo = 0
        self._limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self._transacoes = []
        self.cartoes = []

    def consultar_saldo(self):
        print(f'Seu saldo atual é R${self._saldo:,.2f}')

    def _limite_conta(self):
        self._limite = -1000
        return self._limite

    def fazer_deposito(self, montante):
        self._saldo += montante
        self._transacoes.append((montante, self._saldo, ContaCorrente._data_e_hora()))

    def fazer_saque(self, montante):
        if (self._saldo - montante) < self._limite_conta():
            print('Saldo insuficiente')
            self.consultar_saldo()
        else:
            self._saldo -= montante
            self._transacoes.append((-montante, self._saldo, ContaCorrente._data_e_hora()))

    def consultar_limtite_cheque_especial(self):
        print('Seu limite de Cheque Especial é de R${:,.2f}'.format(self._limite_conta()))

    def consultar_historico_transacoes(self):
        print('Histórico de Transações:')
        for transacao in self._transacoes:
            print(transacao)

    def transferir(self, montante, conta_destino):
        self._saldo -= montante
        self._transacoes.append((-montante, self._saldo, ContaCorrente._data_e_hora()))
        conta_destino._saldo += montante
        conta_destino._transacoes.append((montante, conta_destino._saldo, ContaCorrente._data_e_hora()))


class CartaoCredito:

    @staticmethod
    def _data_e_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = '{}/{}'.format(CartaoCredito._data_e_hora().month, CartaoCredito._data_e_hora().year + 4)
        self.cod_seguranca = '{}{}{}'.format(randint(0, 9), randint(0, 9), randint(0, 9))
        self._senha = '1234'
        self.limite = 1000
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
            print('Senha alterada com sucesso!')
        else:
            print('Nova senha inválida.')

