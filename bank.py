from datetime import datetime
import pytz

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
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._limite = None
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []

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

    def __init__(self, titular, conta_corrente):
        self.numero = None
        self.titular = titular
        self.validade = None
        self.cod_seguranca = None
        self.limite = None
        self.conta_corrente = conta_corrente


# programa 1

conta_kaio = ContaCorrente('Kaio Pedreira', '111.222.333-44', 1234, 56789)
#
# conta_kaio.consultar_saldo()
#
# # deposito
# conta_kaio.fazer_deposito(10000)
# conta_kaio.consultar_saldo()
#
# # sacando
# conta_kaio.consultar_limtite_cheque_especial()
#
# print('-' * 20)
# print(conta_kaio.consultar_historico_transacoes())
#
# print('-' * 20)
# conta_mae_kaio = ContaCorrente('Dona Lili', '00000000000', 4321, 43321)
# conta_kaio.transferir(1000, conta_mae_kaio)
#
# conta_kaio.consultar_saldo()
# conta_mae_kaio.consultar_saldo()
# print('-' * 20)
# conta_kaio.consultar_historico_transacoes()
# conta_mae_kaio.consultar_historico_transacoes()

# programa 2

cartao_kaio = CartaoCredito('Kaio', conta_kaio)

print(cartao_kaio.conta_corrente._num_conta)