from bank import ContaCorrente, CartaoCredito
from agencia import Agencia, AgenciaComum, AgenciaPremium, AgenciaVirtual

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

# print(cartao_kaio.conta_corrente._agencia)

# print(conta_kaio.cartoes[0].numero)
#
# print(cartao_kaio.validade)
#
# print(cartao_kaio.cod_seguranca)

cartao_kaio.senha = '12'

print(cartao_kaio.senha)

print('-' * 20)

print(conta_kaio.__dict__)

print(cartao_kaio.__dict__)

agencia1 = Agencia(22224444, 9080702, 123)

agencia1.caixa = 2000000

# agencia1.verificar_caixa()

# agencia1.emprestar_dinheiro(1500, 11122233344, 0.02)
#
# print(agencia1.emprestimos)

# agencia1.adicionar_cliente('kaio', 11122233344, 400)
#
# print(agencia1.clientes)
#
agencia_virtual = AgenciaVirtual('www.agvirtual.br', 11112222, 298432094820)

# agencia_comum = AgenciaComum(88889999, 8324843893)
#
# agencia_comum.verificar_caixa()

agencia_premium = AgenciaPremium(55556666, 89791739817)
# agencia_premium.verificar_caixa()
#
# agencia_virtual.depositar_paypal(20000)
# print(agencia_virtual.caixa_paypal)

agencia_premium.adicionar_cliente('Kaio', 2222222, 3000000)

print(agencia_premium.clientes)