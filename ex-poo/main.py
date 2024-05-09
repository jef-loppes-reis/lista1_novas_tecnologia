from modules.cliente import Cliente
from modules.conta import Conta
from modules.conta_corrente import ContaCorrente


cliente = Cliente('Jeferson', 'Lopes', '00000-9')
conta = Conta('894-7', 'Corrente', cliente, 40_000.00, 15_000.00)

print(f'Saldo da conta corrente: R$ {conta.saldo:.2f}')
conta._historico.imprime()
